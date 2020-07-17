#5.10: Code Challenge: Solve the Local Alignment Problem.

import numpy as np
import sys
sys.setrecursionlimit(100000000)

#made by dennis kenbeek (4686357)

def MakeMatrices(data, scores, sigma):
    scoreRef = scores[0]
    scoreRef = scoreRef.split(' ')
    filter_object = filter(lambda x: x != "", scoreRef)
    scoreRef = np.asarray(list(filter_object))
    
    scoreMatrix = np.zeros((len(scoreRef),len(scoreRef)),)
    
    for i in range(0, len(scoreMatrix)):
        row = list(filter(lambda x: x != "", scores[i+1].split(' ')[1:]))
        scoreMatrix[i][:] = row
        
    #use s1 for the rows, and s2 for the columns
    v = data[0] #n
    w = data[1] #m
    Down = np.zeros((len(v), len(w)+1),)
    Down[:][:] = -sigma
    Right = np.zeros((len(v)+1, len(w)),)
    Right[:][:] = -sigma
    
    return v, w, len(v), len(w), Down, Right, scoreMatrix, scoreRef

def OutputLCS(backtrack, v, w, v_list, w_list, i, j):
    if i <= 0 or j <= 0:
        return 
    if backtrack[i][j] == 1:
        OutputLCS(backtrack, v, w, v_list, w_list, i-1, j)
        v_list.append(v[i-1])
        w_list.append('-')
    elif backtrack[i][j] == 2:
        OutputLCS(backtrack, v, w, v_list, w_list, i, j-1)
        v_list.append('-')
        w_list.append(w[j-1])
    elif backtrack[i][j] == 3:
        OutputLCS(backtrack, v, w, v_list, w_list, i-1, j-1)
        v_list.append(v[i-1])
        w_list.append(w[j-1])
    else:
        return
def LCSBackTrack(data, scores, sigma):
    v, w, n, m, Down, Right, scoreMatrix, scoreRef = MakeMatrices(data, scores, sigma) 
    s = np.zeros((n+1,m+1), dtype=int)
    backtrack = np.zeros((n+1,m+1), dtype=int)

    for i in range(1,n+1):
        for j in range(1,m+1):
            
            v_pos = np.where(scoreRef == v[i-1])[0][0]
            w_pos = np.where(scoreRef == w[j-1])[0][0]
            
            scores = [0, s[i-1][j] + Down[i-1][j], s[i][j-1] + Right[i][j-1], s[i-1][j-1] + scoreMatrix[v_pos][w_pos]]
            s[i][j] = max(scores)

            backtrack[i][j] = scores.index(s[i][j]) #assign 0,1,2,3
                 
    v_list = []
    w_list = []
    str(OutputLCS(backtrack, v, w, v_list, w_list, np.where(s == np.amax(s))[0][0], np.where(s == np.amax(s))[1][0]))
    print(s[np.where(s == np.amax(s))[0][0]][np.where(s == np.amax(s))[1][0]])
    print(*v_list,sep='')
    print(*w_list,sep='')
    
f = open("/Users/denniskenbeek/Downloads/dataset_327658_10.txt", "r")
data = f.read().split('\n')
f.close()

f = open("/Users/denniskenbeek/Downloads/PAM250.txt", "r")
PAM250 = f.read().split('\n')
f.close()

sigma = 5
LCSBackTrack(data, PAM250, sigma)

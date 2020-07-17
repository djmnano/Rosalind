#5.10: Code Challenge: Solve the Global Alignment Problem.

import numpy as np

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
    v = data[1] #n
    w = data[0] #m
    Down = np.zeros((len(v), len(w)+1),)
    Down[:][:] = -sigma
    Right = np.zeros((len(v)+1, len(w)),)
    Right[:][:] = -sigma

    return v, w, len(v), len(w), Down, Right, scoreMatrix, scoreRef

def OutputLCS(backtrack, v, w, v_list, w_list, i, j):
    if i == 0 or j == 0:
        return 
    if backtrack[i][j] == 1:
        OutputLCS(backtrack, v, w, v_list, w_list, i-1, j)
        v_list.append(v[i-1])
        w_list.append('-')
    elif backtrack[i][j] == 2:
        OutputLCS(backtrack, v, w, v_list, w_list, i, j-1)
        v_list.append('-')
        w_list.append(w[j-1])
    else:
        OutputLCS(backtrack, v, w, v_list, w_list, i-1, j-1)
        v_list.append(v[i-1])
        w_list.append(w[j-1])
    
def LCSBackTrack(data, scores, sigma):
    v, w, n, m, Down, Right, scoreMatrix, scoreRef = MakeMatrices(data, scores, sigma)
    s = np.zeros((n+1,m+1), dtype=int)
    backtrack = np.zeros((n+1,m+1), dtype=int)
    
    #make the initial steps down and to the right and add penalty sigma
    for i in range(1,n+1):
        s[i][0] = s[i-1][0] + Down[i-1][0]
    for j in range(1,m+1):
        s[0][j] = s[0][j-1] + Right[0][j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            #get the positions in the BLOSUM matrix
            v_pos = np.where(scoreRef == v[i-1])[0][0]
            w_pos = np.where(scoreRef == w[j-1])[0][0]
            
            s[i][j] = max([s[i-1][j] + Down[i-1][j], s[i][j-1] + Right[i][j-1], s[i-1][j-1] + scoreMatrix[v_pos][w_pos]])

            if s[i][j] == s[i-1][j] + Down[i-1][j]:
                backtrack[i][j] = 1
            elif s[i][j] == s[i][j-1] + Right[i][j-1]:
                backtrack[i][j] = 2
            else:
                backtrack[i][j] = 3
    print(backtrack)   
    v_list = []
    w_list = []

    str(OutputLCS(backtrack, v, w, v_list, w_list, n, m))
    print(s[n][m])
    print(*w_list,sep='')
    print(*v_list,sep='')
    
f = open("/Users/denniskenbeek/Downloads/dataset_327658_3.txt", "r")
data = f.read().split('\n')
f.close()

f = open("/Users/denniskenbeek/Downloads/BLOSUM62.txt", "r")
BLOSUM62 = f.read().split('\n')
f.close()

sigma = 5
LCSBackTrack(data, BLOSUM62, sigma)

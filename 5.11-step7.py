#5.11: Code Challenge: Solve the Overlap Alignment Problem.

import numpy as np

#made by dennis kenbeek (4686357)

def OutputLCS(backtrack, v, w, v_list, w_list, i, j):
    if i <= 0 or j <= 0:
        return 
    if backtrack[i][j] == 0:
        OutputLCS(backtrack, v, w, v_list, w_list, i-1, j)
        v_list.append(v[i-1])
        w_list.append('-')
    elif backtrack[i][j] == 1:
        OutputLCS(backtrack, v, w, v_list, w_list, i, j-1)
        v_list.append('-')
        w_list.append(w[j-1])
    else:
        OutputLCS(backtrack, v, w, v_list, w_list, i-1, j-1)
        v_list.append(v[i-1])
        w_list.append(w[j-1])
        
def OverlapAlignment(v, w, sigma, match):
    n = len(v)
    m = len(w)
    
    s = np.zeros((n+1,m+1), dtype=int)

    backtrack = np.zeros((n+1,m+1), dtype=int)
    
    maxScore = None
    maxPos = []
    for i in range(1,n+1):
        for j in range(1,m+1):
            if v[i-1] == w[j-1]:
                x = match
            else:
                x = -sigma
            
            scores = [s[i-1][j] - sigma, s[i][j-1] - sigma, s[i-1][j-1] + x]
            s[i][j] = max(scores)

            backtrack[i][j] = scores.index(s[i][j])
            
            if i == n or j == m:
                if maxScore == None:
                    maxScore = s[i][j]
                    maxPos = [i,j]
                if s[i][j] > maxScore:
                    maxScore = s[i][j]
                    maxPos = [i,j]
             
    v = v[:maxPos[0]]
    w = w[:maxPos[1]]

    v_list = []
    w_list = []
    LCS = str(OutputLCS(backtrack, v, w, v_list, w_list, maxPos[0], maxPos[1]))
    print(s[maxPos[0]][maxPos[1]])
    print(*v_list,sep='')
    print(*w_list,sep='')
    
    return 
    
f = open("/Users/denniskenbeek/Downloads/dataset_327659_7.txt", "r")
data = f.read().split('\n')
f.close()

sigma = 2
match = 1

v = data[0]
w = data[1]

OverlapAlignment(v, w, sigma, match)

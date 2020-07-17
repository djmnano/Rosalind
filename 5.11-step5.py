#5.11: Code Challenge: Solve the Fitting Alignment Problem.

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
def FittingAlignment(data, sigma, match):
    v = data[0]
    w = data[1]
    n = len(v)
    m = len(w)

    s = np.zeros((n+1,m+1), dtype=int)
    backtrack = np.zeros((n+1,m+1), dtype=int)


    for i in range(1,n+1):
        for j in range(1,m+1):
            if v[i-1] == w[j-1]:
                x = match
            else:
                x = -match
            scores = [s[i-1][j] - sigma, s[i][j-1] - sigma, s[i-1][j-1] + x]
            s[i][j] = max(scores)

            backtrack[i][j] = scores.index(s[i][j])
    
    #now we shouldn't start at the max node like in the local alignment
    #we should start at the max node corresponding to the end of w (column = m)
    #the fitting of v should be as least as long as w, so start looking for the max
    #where the rows are == m
    #this is similar to the jumping of local alignment
    
    p = 0
    maxScore = 0
    for row in range(m,n):
        if s[row][m] > maxScore:
            maxScore = s[row][m]
            p = row
    print(p)
    
    v_list = []
    w_list = []
    LCS = str(OutputLCS(backtrack, v, w, v_list, w_list, p, m))
    print(s[p][m])
    print(*v_list,sep='')
    print(*w_list,sep='')
    
f = open("/Users/denniskenbeek/Downloads/dataset_327659_5.txt", "r")
data = f.read().split('\n')
f.close()

sigma = 1
match = 1
FittingAlignment(data, sigma, match)

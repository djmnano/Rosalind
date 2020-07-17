#5.8: Code Challenge: Use OutputLCS (reproduced below) to solve the Longest Common Subsequence Problem

#made by dennis kenbeek (4686357)

import numpy as np
import sys

sys.setrecursionlimit(10**6) 

def MakeMatrices(data):
    #use s1 for the rows, and s2 for the columns
    s1 = data[0] #n
    s2 = data[1] #m
    Down = np.zeros((len(s1), len(s2)+1),)
    Right = np.zeros((len(s1)+1, len(s2)),)
    Diag = np.zeros((len(s1), len(s2)),)
    
    for i in range(0,len(s1)):
        for j in range(0, len(s2)):
            if s1[i] == s2[j]:
                Diag[i][j] = 1
  
    return len(s1), len(s2), Down, Right, Diag

def OutputLCS(backtrack, v, i, j):
    if i == 0 or j == 0:
        return ""
    if backtrack[i][j] == 1:
        return OutputLCS(backtrack, v, i-1, j)
    elif backtrack[i][j] == 2:
        return OutputLCS(backtrack, v, i, j-1)
    else:
        return OutputLCS(backtrack, v, i-1, j-1), v[i-1] 
    
def LCSBackTrack(data):
    n, m, Down, Right, Diag = MakeMatrices(data)
    s = np.zeros((n+1,m+1), dtype=int)
    backtrack = np.zeros((n+1,m+1), dtype=int)
    for i in range(1,n+1):
        s[i][0] = s[i-1][0] + Down[i-1][0]
    for j in range(1,m+1):
        s[0][j] = s[0][j-1] + Right[0][j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i][j] = max(s[i-1][j] + Down[i-1][j], s[i][j-1] + Right[i][j-1],s[i-1][j-1] + Diag[i-1][j-1])
            if s[i][j] == s[i-1][j]:
                backtrack[i][j] = 1
            elif s[i][j] == s[i][j-1]:
                backtrack[i][j] = 2
            elif s[i][j] == s[i-1][j-1]:
                backtrack[i][j] = 3
    LCS = str(OutputLCS(backtrack, data[0], n, m))
    LCS = LCS.replace('(', '')
    LCS = LCS.replace(')', '')
    LCS = LCS.replace(',', '')
    LCS = LCS.replace("'", '')
    LCS = LCS.replace(" ", '')
    return(LCS)
    
f = open("/Users/denniskenbeek/Downloads/dataset_327656_5.txt", "r")
data = f.read().split('\n')
f.close()

print(LCSBackTrack(data))

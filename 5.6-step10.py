#5.6: Code Challenge: Find the length of a longest path in the Manhattan Tourist Problem.

#made by dennis kenbeek (4686357)

import numpy as np

def ManhattenTourist(n, m, Down, Right):
    s = np.zeros((n+1,m+1), dtype=int)
    for i in range(1,n+1):
        s[i][0] = s[i-1][0] + Down[i-1][0]
    for j in range(1,m+1):
        s[0][j] = s[0][j-1] + Right[0][j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i][j] = max(s[i-1][j] + Down[i-1][j], s[i][j-1] + Right[i][j-1])

    return s[n][m]

f = open("/Users/denniskenbeek/Downloads/dataset_327654_10.txt", "r")
data = f.read().split('\n')
f.close()

dim = data[0].split(' ')
n = int(dim[0])
m = int(dim[1])

startpos = 1
Down = np.zeros((n,m+1), dtype = int)
for i in range(0,n):
    s = data[i+startpos].split(' ')
    for j in range(0,len(s)):
        Down[i][j] = int(s[j])
        
startpos += n+1
Right = np.zeros((n+1,m), dtype = int)
for i in range(0,n+1):
    s = data[i+startpos].split(' ')
    for j in range(0,len(s)):
        Right[i][j] = int(s[j])


print(ManhattenTourist(n,m,Down,Right))

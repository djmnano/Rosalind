#5.11: Code Challenge: Solve the Edit Distance Problem.

import numpy as np

#made by dennis kenbeek (4686357)

#now the problem isn't finding the maximum score, but the min, where the penalty for a del/insert/mismatch = 1
def EditDistance(data, dist):
    v = data[1]
    w = data[0]
    n = len(v)
    m = len(w)
    
    s = np.zeros((n+1,m+1), dtype=int)

    for i in range(1,n+1):
        s[i][0] = s[i-1][0] + dist
    for j in range(1,m+1):
        s[0][j] = s[0][j-1] + dist
    for i in range(1,n+1):
        for j in range(1,m+1):

            if v[i-1] == w[j-1]:
                s[i][j] = s[i-1][j-1]
            
            else:
                s[i][j] = min([s[i-1][j] + dist, s[i][j-1] + dist, s[i-1][j-1]+dist])

    return s[n][m]
    
f = open("/Users/denniskenbeek/Downloads/dataset_327659_3.txt", "r")
data = f.read().split('\n')
f.close()

dist = 1

print(EditDistance(data, dist))

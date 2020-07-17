#7.3 Code Challenge: Solve the Limb Length Problem.
import numpy as np

#made by dennis kenbeek (4686357)

def MakeMatrix(data, leaves):
    matrix = np.zeros((leaves,leaves))
    matrixText = []
    for i in range(leaves):
        text = data[i].split(' ')
        for j in range(leaves):
            matrix[i][j] = int(text[j])
    return matrix

def getLimbLength(leaves, distanceMatrix, j):
    LimbLength = None

    for i in range(leaves):
        for k in range(leaves):
            if j != k and i != j and k != i:
                x = distanceMatrix[i][j] + distanceMatrix[j,k] - distanceMatrix[i,k]
                if LimbLength == None or x/2 < LimbLength:
                    LimbLength = x/2
    return LimbLength      
f = open("/Users/denniskenbeek/Downloads/dataset_327692_11.txt", "r")
data = f.read().split('\n')
f.close()

leaves = int(data[0])
j = int(data[1])

matrix = MakeMatrix(data[2:],leaves)

LimbLength = getLimbLength(leaves, matrix, j)

print(int(LimbLength))

import numpy as np
import random

#Made by Dennis Kenbeek (4686357)

def MakeMatrix(data, m):
    matrix = np.zeros((len(data),m),)

    for i in range(len(data)):
        s = data[i].split(' ')
        for ii in range(m):
            matrix[i][ii] = s[ii]
    
    return matrix

def MaxDistance(matrix, m, centers, used):

    #distances map tracks all distances to each data point for each center
    distances = {}

    #go through all data points
    for i in range(len(matrix)):
        coords = matrix[i][:]
        distList = []

        #go through all centers
        for x in centers:
            #get the distance
            x = np.array(x)
            dist = np.linalg.norm(x-coords)
            if dist != 0: #make sure you aren't registering distance to itself
                distList.append(dist)

        #take the minimum from these distances, according to the definition used
        if not distList:
            distances[i] = dist
        else:
            distances[i] = min(distList)

    #from all of these distances choose the one maximum position
    maxDist = 0
    for i in range(len(distances)):
        dist = distances[i]
        if dist > maxDist and i not in used:
            maxDist = dist
            newPoint = matrix[i][:]
            final = i
    #keep track of the used datapoint
    used.append(final)
    return used, newPoint

def FarthestFirstTraversal(matrix, m):
    #initiate the first center
    centers = [matrix[0][:]]

    used = [0] #keep track of the rows used
    while len(centers) < k:
        used, point = MaxDistance(matrix, m, centers, used)

        centers += [point.tolist()]
    
    return centers

f = open("/Users/denniskenbeek/Downloads/dataset_327715_2.txt", "r")
data = f.read().split('\n')
f.close()

if '' in data:
    data.remove('')

s = data[0].split(' ')
k = int(s[0])
m = int(s[1])

matrix = MakeMatrix(data[1:],m)

centers = FarthestFirstTraversal(matrix, m)

for x in centers:
    print(*np.array(x).tolist(), sep=' ')


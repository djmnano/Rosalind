
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

def Lloyd(matrix, k,m):
    
    centers = []
    for i in range(k):
        centers.append(matrix[i][:].tolist())    

    random.shuffle(centers)

    changing = True

    while changing == True:

        clusters = {}
        #assign points to nearest center
        for i in range(len(matrix)):
            coords = matrix[i][:]
            dist = []
            for ii in range(k):
                dist.append(np.linalg.norm(coords - centers[ii])) #get distance for this coordinate to each cluster
            
            #add this coordinate to cluster with minimum distance
            #i use dist.index to find the position of the cluster with min distance, as we go through them in order anyway
            if dist.index(min(dist)) not in clusters:
                clusters[dist.index(min(dist))] = [coords.tolist()]
            else:
                clusters[dist.index(min(dist))] += [coords.tolist()]

        newCenters = []
        for i in range(len(clusters)):
            newCenters.append(np.mean(clusters[i],0).tolist()) #new clusters are equal to the mean of the assigned datapoints
        
        #check if they converged or not
        if newCenters == centers:
            changing = False
        else:
            centers = newCenters

    for x in centers:
        x = np.round(x, 3)
        print(*x, sep = ' ')

f = open("/Users/denniskenbeek/Downloads/dataset_327717_3.txt", "r")
data = f.read().split('\n')
f.close()

if '' in data:
    data.remove('')

s = data[0].split(' ')
k = int(s[0])
m = int(s[1])

matrix = MakeMatrix(data[1:],m)

Lloyd(matrix,k,m)
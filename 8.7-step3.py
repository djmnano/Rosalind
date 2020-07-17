
import numpy as np

#Made by Dennis Kenbeek (4686357)

def MakeMatrix(data, m):
    matrix = np.zeros((len(data),m),)
    
    for i in range(len(data)):
        s = data[i].split(' ')
        for ii in range(m):
            matrix[i][ii] = s[ii]
    
    return matrix


def d(datapoint, centers):

    distList = []
    #for each point in centers calculate the distance
    for x in centers:
        x = np.array(x)
        dist = np.linalg.norm(x-datapoint)
        if dist != 0:
            distList.append(dist)

    #choose the minimum
    if not distList:
        return dist
    else:
        return min(distList)


def Distortion(datapoints, centers):
    distList = []
    #go through all datapoints
    for x in datapoints:
        #get the distance and square it
        distList.append(d(x,centers)**2)
    
    distortion = 1/len(datapoints)*np.sum(distList)
    print("%.3f" % distortion)


f = open("/Users/denniskenbeek/Downloads/dataset_327716_3.txt", "r")
data = f.read().split('\n')
f.close()

if '' in data:
    data.remove('')

s = data[0].split(' ')
k = int(s[0])
m = int(s[1])

for i in range(len(data)):
    if data[i] == '--------':
        break


centers = MakeMatrix(data[1:i], m)
datapoints = MakeMatrix(data[i+1:], m)
Distortion(datapoints, centers)
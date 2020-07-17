import numpy as np

#made by dennis kenbeek (4686357)

def MakeMatrix(connections, leaves):

    weightsMap = {}
    
    conMap = {}

    for x in connections:
        s = x.split('->')
        r = int(s[0]) #row
        c = int(s[1].split(':')[0]) #column
           
        weightsMap[r,c] = int(s[1].split(':')[1])   
        
        if r in conMap:
            conMap[r] += [c]
        else:
            conMap[r] = [c]

    return conMap, weightsMap


def fillDistanceMap(start, con, conMap, leaves, distanceMap, weight, weightsMap, lastStep):
    edges = conMap[con] #get the connections
    for x in edges:
        if x == lastStep: #we don't want it to go back
            continue
        elif x in range(leaves): #we found a leave
            weight += weightsMap[con,x] 
            distanceMap[start,x] = weight #register the distance
            weight -= weightsMap[con,x] #backtrack, so you don't count it for others
        else: #use recursion to do the same thing for the other internal nodes
            weight += weightsMap[con,x]
            fillDistanceMap(start, x, conMap, leaves,  distanceMap, weight, weightsMap, con)
            weight -= weightsMap[con,x]
            
def MakeDistanceMatrix(weightsMap, leaves, conMap):
    
    distanceMatrix = np.zeros((leaves,leaves), dtype=int)
    distanceMap = {}

    for i in range(leaves):
        con = conMap[i][0] #get the connection to inner node
	
	#for each leave we get the distances to all other leaves, by backtracking over the inner nodes
        weight = weightsMap[i,con]
        fillDistanceMap(i, con, conMap, leaves, distanceMap, weight, weightsMap, i)
    
    #transform the distancemap into the distance matrix    
    for x in distanceMap:
        i = x[0]
        j = x[1]
        distanceMatrix[i][j] = distanceMap[x]
    
    for i in range(leaves):
        for j in range(leaves):
            print(distanceMatrix[i][j], end=' ')
        print('\n')
        
f = open("/Users/denniskenbeek/Downloads/dataset_327691_12.txt", "r")
data = f.read().split('\n')
f.close()

if '' in data:
    data.remove('')
leaves = int(data[0])

conMap, weightsMap = MakeMatrix(data[1:], leaves)

MakeDistanceMatrix(weightsMap, leaves, conMap)

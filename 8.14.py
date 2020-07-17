import numpy as np
import itertools

def MakeMatrix(data, leaves):
    matrix = np.zeros((leaves,leaves))
    for i in range(leaves):
        text = data[i].split(' ')
        for j in range(leaves):
            matrix[i][j] = float(text[j])
    return matrix

def findClosest(D, skip):
    (x,y) = (0,0)
    lowest = 10000
    for i in range(0,len(D)):
        for ii in range(0,i): #the matrix is symmetric
            if D[i][ii] < lowest and D[i][ii] != 0 and i not in skip and ii not in skip:
                (x,y) = (i,ii)
                lowest = D[i][ii]
    return (x,y)

def HierarchicalClustering(D, names):

    #keep track of clusters
    Clusters = []
    ClustersMap = {}
    for i in range(0,len(D)):
        Clusters.append([i])
        ClustersMap[i] = [i]

    #initialize a list of nodes to skip
    skip = []
    while len(Clusters) >= 2:
          
        (Ci, Cj) = findClosest(D, skip)
    
        Ci_con = D[Ci][:]
        Cj_con = D[Cj][:]
        newRow = []
        #we construct a new row based on Ci and Cj
        for i in range(0,len(Ci_con)):
            if Ci_con[i] != 0 and Cj_con[i] != 0:
                newRow.append((Ci_con[i]*len(ClustersMap[Ci])+Cj_con[i]*len(ClustersMap[Cj]))/(len(ClustersMap[Ci])+len(ClustersMap[Cj])))
            else:
                newRow.append(0)
        
        #put the new row at Cj and add Ci to the skip list, this won't be taken into account anymore 
        D[Cj][:] = newRow
        for i in range(0,len(D)):
            D[i][Cj] = newRow[i]

        skip.append(Ci)

        #delete the previous clusters and combine them into a new one
        Clusters.remove(ClustersMap[Cj])
        Clusters.remove(ClustersMap[Ci])
        Clusters.append(ClustersMap[Ci] + ClustersMap[Cj])
        
        ClustersMap[Cj] = ClustersMap[Ci] + ClustersMap[Cj]
        
        newCluster = []
        for x in ClustersMap[Cj]:
            newCluster.append(x+1)
        print(*newCluster)
    
    return 
    
f = open("/Users/denniskenbeek/Downloads/rosalind_ba8e.txt", "r")
data = f.read().split('\n')
f.close()

leaves = int(data[0])

matrix = MakeMatrix(data[1:],leaves)
names = leaves

HierarchicalClustering(matrix,names)

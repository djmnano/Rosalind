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

            
def insertConnection(T, names, Cj, Dist):
    
    #get the correct name for the new node
    for x in T:
        for con,weight in T[x]:
            if con >= names:
                names += 1

    #repr() function allows us to use the clusters in our tree directly
    if repr(Cj) in T:
        T[repr(Cj)] += [(names, Dist/2)]
    else:
        T[repr(Cj)] = [(names, Dist/2)]
    
def checkLast(T, con):

    nextNode = False

    weight = 0

    #we loop through the connections of the node
    #if it has a connection to a node with a higher value we continue, and keep track of the weights
    #once we can't find one we break the loop

    while True:
        nextNode = False
        for x,w in T[con]:
            if x in T and x > con:
                nextNode = True
                weight = weight+w
                break
                
        if nextNode == True:
            con = x
        else:
            break
        
    return con, weight

def UPGMA(D, names):

    #keep track of clusters
    Clusters = []
    ClustersMap = {}
    for i in range(0,len(D)):
        Clusters.append([i])
        ClustersMap[i] = [i]

    #initialize the tree and a list of nodes to skip
    T = {}
    skip = []
    while len(Clusters) >= 2:
          
        (Ci, Cj) = findClosest(D, skip)

        Dist = D[Ci][Cj]
    
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
       
        #insert this into the Tree at distance Dist
        insertConnection(T, names, ClustersMap[Cj], Dist)
    
  
    #from the previous tree which has clusters we make the final Tree

    T_final = {}

    #for each connection in T (which are clusters) make the final tree
    for x in T:
        
        #the following steps are to make it into an integer array
        p = x.split(' ')
       
        for i in range(len(p)):
            y = p[i]
            if not y.isdigit():
                if i == 0:
                    y = y[1:-1]
                else:
                    y = y[:-1]   
            else:
                p[i] = y
            p[i] = y

        #go through the connections of this cluster
        for con, weight in T[x]:
 
            for nodes in p:

                node = int(nodes)

                #if this node isn't in final tree, we add it with the current connection
                if node not in T_final:
                    T_final[node] = [(con, weight)]
                    if con not in T_final:
                        T_final[con] = [(node, weight)]
                    else:
                        T_final[con] += [(node, weight)]

                #if it is in the final tree, we go through it to find the last connection
                #we continue from the last connection to go the next one 
                else:
                    v,w = checkLast(T_final,node)
           
                    if (con, weight - w) not in T_final[v]:
                        T_final[v] += [(con, weight - w)]
                    if con not in T_final:
                        T_final[con] = [(v, weight - w)]
                    else:
                        T_final[con] += [(v, weight - w)]
                    
           
    return T_final
    
f = open("/Users/denniskenbeek/Downloads/dataset_327723_7.txt", "r")
data = f.read().split('\n')
f.close()

leaves = int(data[0])

matrix = MakeMatrix(data[1:],leaves)
names = leaves

T = UPGMA(matrix,names)

c = 0 

done = False
while not done:
    if c in T:
        for con, weight in T[c]:
            if c != con:
                print(str(c)+ '->' + str(con)+':'+ f'{10*weight:01f}')
    else:
        done = True 
    
    c = c + 1
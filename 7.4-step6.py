import numpy as np

#Made by Dennis Kenbeek (4686357)

def getLimbLength(distanceMatrix, leaves, j):
    LimbLength = None

    for i in range(leaves):
        for k in range(leaves):
            if j != k and i != j and k != i:
                x = distanceMatrix[i][j] + distanceMatrix[j][k] - distanceMatrix[i][k]
                if LimbLength == None or x/2 < LimbLength:
                    LimbLength = x/2
    return LimbLength     

#tranform input into matrix
def MakeMatrix(data, leaves):
    matrix = np.zeros((leaves,leaves))
    for i in range(leaves):
        text = data[i].split(' ')
        for j in range(leaves):
            matrix[i][j] = int(text[j])
    return matrix

#function to find (i, k) ← two leaves such that Di,k = Di,n + Dn,k
def findIKN(D,n):
    for i in range(n):
        for k in range(n):
            if D[i][k] == D[i][n-1]+D[n-1][k] and i != k:
                return(i,k)


def getPath(T, i, k, visited):

    visited[0][i] = 1
    
    for conn in T[i]:

        #keep track of visited otherwise we go over recursion limit
        if visited[0][conn] == 1: 
            continue

        # if end is found, return that edge.
        if conn == k:
            return [i, k]

        # recursively call getPath with v as start and see if v is on the path to k.
        path = getPath(T, conn, k, visited)
        if path != False:
            path.insert(0,i)
            return path

    # if i is not on the path to k, return None.
    return False
            

def insertV(T_con, T_weights, i, k, x, n, visited,startName, limbLength):
    #get the path from i to k

    path = getPath(T_con, i, k, visited)

    if path is not False:
        relativePos = 0

        #find place to put v
        for i in range(1,len(path)):
            node = path[i-1]
            for conn in T_con[node]:
                if conn == path[i]:
                    weight = T_weights[(node,conn)]

            if x >= weight:
                x = x - weight
                relativePos = relativePos + 1
            else:
                break
        
        v = path[relativePos]
        nodeAfterV = path[relativePos+1]

        #name starts at leaves, count how many internal nodes we already have
        name = startName
        for y in T_con:
            if y == name:
                name = y+1
        
        #add new node at distance x
        T_con[v].append(name)
        T_weights[(v,name)] = x
        T_weights[(name,v)] = x

        #find original weight between v and nodeAfterV    
        for conn in T_con[nodeAfterV]:
            if conn == v:
                weight = T_weights[(nodeAfterV,v)]

        #the connection between v and nodeAfterV needs to be split up
        T_con[nodeAfterV].append((name))
        T_weights[(nodeAfterV, name)] = weight - x
        T_weights[(name,nodeAfterV)] = weight - x
        
        #make the new node and add back leave n with limbLength
        T_con[name] = [v, nodeAfterV, n-1]
        T_con[n-1] = [name]
        T_weights[(n-1,name)] = limbLength
        T_weights[(name,n-1)] = limbLength

        #loop through connections to find the original connection between v and nodeAfterV
        #we should delete those
        connections = T_con[v]
        for i in range(0, len(connections)):
            if connections[i] == nodeAfterV:
                del T_con[v][i]     
                break
        connections = T_con[nodeAfterV]
        for i in range(0, len(connections)):
            if connections[i] == v:
                del T_con[nodeAfterV][i]    
                break

def AdditivePhylogeny(D, names):
    n = len(D)
    if n == 2:
        return  {0: [1], 1: [0]}, {(0,1): D[0][1], (1,0): D[0][1]}

    limbLength = getLimbLength(D,n, n-1) #limblength of last leave

    for j in range(0,n-1):
        D[j][n-1] = D[j][n-1]-limbLength
        D[n-1][j] = D[j][n-1]

    (i,k) = findIKN(D,n)

    x = D[i][n-1]
    newD = np.zeros((n-1, n-1), dtype=int)

    for j in range(n-1):
        for jj in range(n-1):
            newD[j][jj] = D[j][jj]
    D = newD
    
    T_con, T_weights = AdditivePhylogeny(D, names)

    # somewhere between (i, k) we need to place a new node v at distance x.

    #get the highest node currently in the tree for the size of visited matrix
    highestNode = 0
    for y in T_con:
        if y > highestNode:
            highestNode = y

    visited = np.zeros((1, highestNode+1), dtype=int)
    insertV(T_con, T_weights, i, k, x, n, visited, names, limbLength)
    
    return T_con, T_weights

f = open("/Users/denniskenbeek/Downloads/dataset_327694_6.txt", "r")
data = f.read().split('\n')
f.close()

leaves = int(data[0])

matrix = MakeMatrix(data[1:],leaves)
names = leaves

T_con, T_weights = (AdditivePhylogeny(matrix,names))

for x in T_con:
    for con in T_con[x]:
        print(str(x)+ '->' +str(con)+':'+ str(int(T_weights[(x,con)])))
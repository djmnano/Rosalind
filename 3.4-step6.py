#3.4 de bruijn

#made by dennis kenbeek (4686357)

import numpy as np

def getKmers(text,k):
    kmers = []
    for i in range(0,len(text)-k+1):
        kmers.append(text[i:i+k])
    return kmers

def deGruijnGraph(text,k):
    #The nodes of the De Gruijn Graph are the k-1mers
    nodesList = []

    #get list of all kmers to make edges
    edgeList = getKmers(text,k)
    
    
    #match all the edges to its nodes
    edgesMap = {}
    
    for x in edgeList:
        nodes = getKmers(x,k-1)
        nodesList.append(nodes)
        if x not in edgesMap:
            edgesMap[x] = [nodes[0], nodes[1]]
        else:
            edgesMap[x] += [nodes[0], nodes[1]]
    
    #use this to make graph
    graphMap = {}
    for x in edgesMap:
        nodes = np.array(edgesMap[x])
        firstNodeNum = np.where(nodes == nodes[1])[0]
        for i in range(0,len(firstNodeNum)): #if there are more
            if nodes[0] not in graphMap:
                graphMap[nodes[0]] = [nodes[1]]
            else:
                graphMap[nodes[0]] += [nodes[1]]
        
    graph = ''
    for x in graphMap:
        graph += x + ' -> ' + ', '.join(graphMap[x]) + '\n'
    print(graph)
    
    f = open("answer3.4.6.txt", "w+")
    f.write(graph)
    return 

f = open("/Users/denniskenbeek/Downloads/dataset_327609_6.txt", "r")
data = f.read().split('\n')
f.close()

k = int(data[0])
text = data[1]

deGruijnGraph(text,k)

#3.8 Code Challenge: Solve the k-Universal Circular String Problem.

#made by dennis kenbeek (4686357)

import numpy as np
import itertools

def getKmersBinary(comb,k):
    kmers = []

    for x in comb:
        kmer = ""
        for i in range(0,len(x)):
            kmer += str(x[i])
        kmers.append(kmer[:])
 
    return kmers

def getKmers(text,k):
    kmers = []
    for i in range(0,len(text)-k+1):
        kmers.append(text[i:i+k])
    return kmers

def deGruijnGraph(kmers,k):
    #The nodes of the De Gruijn Graph are the k-1mers
    nodesList = []

    #get list of all kmers to make edges
    edgeList = kmers
    
    #match all the edges to its nodes
    edgesMap = {}
    
    symmetricalCount = {}
    for x in edgeList:
        nodes = getKmers(x,k-1)
        nodesList.append(nodes)
        if x not in edgesMap:
            edgesMap[x] = [nodes[0], nodes[1]]
        else:
            edgesMap[x] += [nodes[0], nodes[1]]
        if nodes[0] == nodes[1]:
            if nodes[0] not in symmetricalCount:
                symmetricalCount[nodes[0]] = 1
            else:
                symmetricalCount[nodes[0]] += 1
    
    #use this to make the graph
    graphMap = {}

    for x in edgesMap:
        nodes = np.array(edgesMap[x])
        
        firstNodeNum = np.where(nodes == nodes[1])[0]
        counter = 0
        for i in range(0,len(firstNodeNum)): #if there are more
            if nodes[0] == nodes[1]:
                counter += 1
                if counter > symmetricalCount[nodes[0]]:
                    break
            if nodes[0] not in graphMap:
                graphMap[nodes[0]] = [nodes[1]]
            else:
                graphMap[nodes[0]] += [nodes[1]]      
   
    graph = ''
    for x in graphMap:
        graph += x + ' -> ' + ', '.join(graphMap[x]) + '\n'
  
   
    return graph

#Eulerian Path
def MakeMatrix(edges):
    inCounterMap = {}
    outCounterMap = {}
    allValuesList = []
    
    #check the highest number so we make the right size matrix
    maxsize = 0
    for x in edges:
        s = x.split(' ')
        i = int(s[0]) #row
        c = s[-1] #column
        c = c.split(',')
        for y in c:
            if int(y) > maxsize:
                maxsize = int(y)
        if i > maxsize:
            maxsize = i
            
    maxsize = int(maxsize)+1
    matrix = np.zeros((maxsize, maxsize),dtype=int)
    
    doubleMap = {}
    doubleCounter = {}
    #go through all the numbers and make the matrix
    for x in edges:
        s = x.split(' ')
        r = int(s[0]) #row
        c = s[-1] #column
        #in case the string has something like 1 -> 2,5
        if ',' in c:
            c = c.split(',')
            placeholder = []
            for y in c:
                if y in placeholder:
                    doubleMap[r,int(y)] = True
                    if (r,int(y)) not in doubleCounter:
                        doubleCounter[r,int(y)] = 2
                    else:
                        doubleCounter[r,int(y)] += 1
                else:
                    placeholder.append(y)
                matrix[r][int(y)] = 1
                if r in outCounterMap:
                    outCounterMap[r] += 1
                else:
                    outCounterMap[r] = 1
                if int(y) in inCounterMap:
                    inCounterMap[int(y)] += 1
                else:
                    inCounterMap[int(y)] = 1
                if int(y) not in allValuesList:
                    allValuesList.append(int(y))
        else:
            matrix[r][int(c)] = 1
            outCounterMap[r] = 1
            if int(c) in inCounterMap:
                inCounterMap[int(c)] += 1
            else:
                inCounterMap[int(c)] = 1
            if int(c) not in allValuesList:
                    allValuesList.append(int(c))
        if r not in allValuesList:
                allValuesList.append(r)

    tooMuchOut = []
    tooMuchIn = []
    notbalancedList = []
    for x in allValuesList:
        if x in inCounterMap:
            if x in outCounterMap:
                if inCounterMap[x] > outCounterMap[x]:
                    tooMuchIn.append(x)
                    notbalancedList.append(x)
                elif inCounterMap[x] < outCounterMap[x]:
                    tooMuchOut.append(x)
                    notbalancedList.append(x)
            else:
                tooMuchIn.append(x)
                notbalancedList.append(x)
        else:
            if x in outCounterMap:
                tooMuchOut.append(x)
                notbalancedList.append(x)
    column = 0
    row = 0
    for x in notbalancedList:
        if x in tooMuchOut:
            column = x
        if x in tooMuchIn:
            row = x
    
   
    if matrix[row][column] == 1:
        doubleMap[row, column] = True
        doubleCounter[row, column] = 2
    else: 
        matrix[row][column] = 1

    startPos = [row, column]
  
    return Cycles(matrix, column, row, startPos, doubleMap,  doubleCounter)

def Cycles(matrix, column, row, startPos, doubleMap, doubleCounter):
    unusedDict = {}
    unusedList = []
    cycleList = []
    
    #check for all if they have multiple edges they can use
    for i in range(0,len(matrix)):
        adjacent = np.where(matrix[i][:] == 1)
        if len(adjacent[0]) > 1:
            for x in adjacent[0]:
                unusedDict[i, x] = True
                unusedList.append([i,x])
    
    cycle = [] #to store the cycle
    
    unusedEdges = True #we use this counter to check for unused edges
    startValue = startPos[0]
    while unusedEdges:
        unusedEdges = False
        for x in unusedList:
            if unusedDict[x[0],x[1]] == True:
                unusedEdges = True
            if (x[0], x[1]) in doubleMap:
                if doubleMap[x[0], x[1]] == True:
                    unusedEdges = True  
        #positions in the matrix
        i = startPos[0]
        ii = startPos[1]
            
        #make sure won't change ii to 0 in the beginning
        start = True
            
        #switch is used to switch to different unused edge
        switch = False
            
        while i < len(matrix):  
            if start == False:
                ii = 0
            while ii < len(matrix):
                if matrix[i][ii] != 0: #we found a connection
                    #change to 0 because we used it
                    matrix[i,ii] = 0
                    unusedDict[i, ii] = False
                    
                    if (i, ii) in doubleMap:
                        if doubleMap[i,ii] == True:
                            if doubleCounter[i,ii] > 1:
                                 matrix[i,ii] = 1
                            doubleCounter[i,ii] += -1
                            if doubleCounter[i,ii] <= 1:
                                doubleMap[i,ii] = False
                                
                    #add it to cycle
                    if not cycle:
                        cycle += [i] + [ii]
                        startValue = i
                    else:
                        cycle += [ii]     
                        
                    if startValue == cycle[-1]:
                        #we made a loop, check if there were unused edges
                        switch = True
                        for j in range(0,len(matrix)):
                            if (ii,j) in unusedDict:
                                if unusedDict[ii,j] == True:
                                    #if unused edges availabe, dont switch
                                    switch = False
                                    
                        if switch == True:
                            #all edges used from this node, so check all other edges
                            foundEdge = False
                            for j in range(0, len(cycle)-1):
                                if foundEdge == False:
                                    #for each that doesnt have an unsed edge, add it to the start
                                    #we can do this because the start is equal to the end
                                        
                                    i = cycle[-2] #new starting position
                                    cycle = [cycle[-2]] + cycle[:-1]
                                        
                                    for jj in range(0, len(matrix)):
                                        if (i,jj) in unusedDict:
                                            #if the one we have in the end now has unused edges
                                            if unusedDict[i,jj] == True:
                                                ii = 0
                                                foundEdge = True
                                                startValue = i
                                                
                    #make sure we start at the new edge                       
                    if switch == False:
                        i = ii-1#move to new position in the matrix     
                        ii = len(matrix) #break out of this while loop
                    else:
                        switch = False
                    start = False
    
                else:
                    #next in this row
                    ii += 1
                    if ii == len(matrix):
                        #break out if reached end of row
                        i = len(matrix)

            i += 1
    return PrintCycle(cycle, column, row)

def removeExtraEdge(cycle, column, row):
    cycle = np.array(cycle)

    pos = np.where(cycle == row)[0]
    coord = []
    for x in pos:
        if cycle[x+1] == column:
            coord = x
            break

    cycleFinal= []
    
    cycleFinal.append(list(cycle[coord+1:]))
    cycleFinal.append(list(cycle[1:coord+1]))
    
    cycleFinal = cycleFinal[0] + cycleFinal[1]

    return cycleFinal
def PrintCycle(cycle, column, row):
    cycle = removeExtraEdge(cycle, column, row)
    string = str(cycle[0]) + "->"
    for i in range(1,len(cycle)-1):
        string += str(cycle[i]) + "->"
        
    string += str(cycle[-1])
 
    return string


f = open("/Users/denniskenbeek/Downloads/dataset_327613_11.txt", "r")
data = f.read().split('\n')
f.close()

k = int(data[0])
comb = list(map(list, itertools.product([0,1], repeat = k)))
binaryKmers= getKmersBinary(comb,k)

graph = deGruijnGraph(binaryKmers,k)

kmersToNumberMap = {}
numberToKmersMap = {}

counter = 0

edgesDNA = graph.split('\n')
edgesDNA = edgesDNA[:-1]
edgesNumbers = []

doublesMap = {}

for x in edgesDNA:
    if ',' in x:
        s1 = x[0:k-1]
        s2 = x[k+2:].split(',')
        if s1 not in kmersToNumberMap:
            kmersToNumberMap[s1] = counter
            numberToKmersMap[counter] = s1
            counter += 1
        placeholder = []
        for y in s2:
            if y[1:] not in kmersToNumberMap:
                kmersToNumberMap[y[1:]] = counter
                numberToKmersMap[counter] = y[1:]
                counter += 1
            

        string = str(kmersToNumberMap[s1]) + ' -> ' + str(kmersToNumberMap[s2[0][1:]])
        for i in range(1,len(s2)):
            string += "," + str(kmersToNumberMap[s2[i][1:]])
        edgesNumbers.append(string)
    else:
        s1 = x[0:k-1]
        s2 = x[k+3:]
        if s1 not in kmersToNumberMap:
            kmersToNumberMap[s1] = counter
            numberToKmersMap[counter] = s1
            counter += 1
        if s2 not in kmersToNumberMap:
            kmersToNumberMap[s2] = counter
            numberToKmersMap[counter] = s2
            counter += 1
        edgesNumbers.append(str(kmersToNumberMap[s1]) + ' -> ' + str(kmersToNumberMap[s2]))

path = MakeMatrix(edgesNumbers)

path = path.split('->')

seqPath = []

for x in path:
    seqPath.append(numberToKmersMap[int(x)])

seq = seqPath[0]
for i in range(1,len(seqPath)-k+1): #leave out the last, to circularize
    seq += seqPath[i][-1]
print(seq)

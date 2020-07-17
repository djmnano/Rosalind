#3.8 Code Challenge: Solve the Eulerian Path Problem.

import numpy as np

#made by dennis kenbeek (4686357)

def MakeMatrix(edges):
    inCounterMap = {}
    outCounterMap = {}
    allValuesList = []
    
    #get the maximum node value so we know the size of our matrix
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
    
    for x in edges:
        s = x.split(' ')
        r = int(s[0]) #row
        c = s[-1] #column
        #in case the string has something like 1 -> 2,5
        if ',' in c:
            c = c.split(',')
            for y in c:
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
                    #imbalanced
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
    
    #find the imbalanced nodes so we know where to start
    for x in notbalancedList:
        if x in tooMuchOut:
            column = x
        if x in tooMuchIn:
            row = x

    matrix[row][column] = 1

    startPos = [row, column]
    Cycles(matrix, column, row, startPos)
    
    return 

def Cycles(matrix, column, row, startPos):
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
    PrintCycle(cycle, column, row)

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
    print(string)

    
f = open("/Users/denniskenbeek/Downloads/dataset_327613_6.txt", "r")
edges = f.read().split('\n')
f.close()

if '' in edges:
    edges.remove('')
cycles = MakeMatrix(edges)

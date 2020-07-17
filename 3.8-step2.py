#3.8 Code Challenge: Solve the Eulerian Cycle Problem.
import numpy as np

#made by Dennis Kenbeek (4686357)
def MakeMatrix(edges):
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
        else:
            matrix[r][int(c)] = 1
  
    return matrix

def Cycles(matrix):
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
    
    startValue = 0
    
    while unusedEdges:
        unusedEdges = False
        
        #start at one with multiple edges
        for x in unusedList:
            if unusedDict[x[0], x[1]] == True:
                unusedEdges = True
            
            #start somewhere (could be random) 
            i = 0
            ii = 0
            
            #used to make sure we won't change ii to 0 in the beginning
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
                        
                        #check if we made a loop
                        if startValue == cycle[-1]:
                            #check if there were unused edges, for this node
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
    PrintCycle(cycle)
def PrintCycle(cycle):
    
    string = str(cycle[0]) + "->"
    for i in range(1,len(cycle)-1):
        string += str(cycle[i]) + "->"
        
    string += str(cycle[-1])
    print(string)

    
f = open("/Users/denniskenbeek/Downloads/dataset_327613_2.txt", "r")
edges = f.read().split('\n')
f.close()

if '' in edges:
    edges.remove('')

matrix = MakeMatrix(edges)
Cycles(matrix)
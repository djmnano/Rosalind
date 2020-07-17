#5.8: Code Challenge: Solve the Longest Path in a DAG Problem.
import numpy as np
import sys

#made by dennis kenbeek (4686357)

def MakeMatrix(connections):

    conIntoMap = {}
    weightsMap = {}
    
    for x in connections:
        s = x.split('->')
        r = int(s[0]) #row
        c = int(s[1].split(':')[0]) #column
        
        if c in conIntoMap:
            conIntoMap[c] += [r]  
            
        else:
            conIntoMap[c] = [r]  
            
        weightsMap[r,c] = int(s[1].split(':')[1])   
    
    return conIntoMap, weightsMap

def PrintBackTrack(start, end, stepTracker):
    backtrack = True
    pos = end
    steps = [pos, stepTracker[pos][0]]
    
    while backtrack == True:
        pos = stepTracker[pos][0]
        if pos in stepTracker:
            steps.append(stepTracker[pos][0])
            if stepTracker[pos][0] == start:
                backtrack = False
        else:
            backtrack = False
        
    steps = steps[::-1]
    for i in range(0,len(steps)-1):
        print(str(steps[i]) + '->', end = '')
    print(steps[-1])
    
def LCSBackTrack(start, end, conIntoMap, weightsMap):
    start = int(start)
    end = int(end)
    maxWeightMap = {}
    
    maxWeightMap[start] = 0
    
    stepTracker = {}
    
    #sort the list because we can assume topological ordering
    order = list(conIntoMap.keys())
    order.sort()
    #go through every node to see which others nodes are connected into it
    #then use the weights to determine the step to take
    for x in order:
        node = conIntoMap[x]
        
        step = []
        for y in node:
            maxWeight = 0
            if x in maxWeightMap:
                maxWeight = maxWeightMap[x]
            if y in maxWeightMap:
                if maxWeightMap[y] + weightsMap[y,x] > maxWeight:
                    maxWeight = maxWeightMap[y] + weightsMap[y,x]
                    step = [y,x]
               
            maxWeightMap[x] = maxWeight   
            stepTracker[x] = step
        
    print(maxWeightMap[int(end)])
    PrintBackTrack(start, end, stepTracker)

f = open("/Users/denniskenbeek/Downloads/dataset_327656_7.txt", "r")
data = f.read().split('\n')
f.close()
print(data)
connections = data[2:-1]
start = data[0]
end = data[1]
conIntoMap, weightsMap = MakeMatrix(connections)

LCSBackTrack(start, end, conIntoMap, weightsMap)

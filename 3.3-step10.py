#3.3 Code challenge: Solve the overlap graph problem

#made by dennis kenbeek (4686357)
import numpy as np

def getKmers(text,k):
    kmers = []
    for i in range(0,len(text)-k+1):
        kmers.append(text[i:i+k])
    return kmers

def OverlapGraph(seqPath, k):
    graph = np.zeros((len(seqPath), len(seqPath)), dtype = int)

    for i in range(0, len(seqPath)):
        suffix_1 = seqPath[i][1:len(seqPath[i])] 
        prefix_1 = seqPath[i][0:len(seqPath[i])-1]
        
        for ii in range(0, len(seqPath)):
            if i != ii:
                suffix_2 = seqPath[ii][1:len(seqPath[ii])] 
                prefix_2 = seqPath[ii][0:len(seqPath[ii])-1]
      
                if suffix_1 == prefix_2: #suffix_1 in front of prefix_2
                    graph[i][ii] == 1
                
                if suffix_2 == prefix_1: #suffix_2 in front of prefix_1
                    graph[ii][i] = 1
        
    return PrintResult(graph, seqPath)

def PrintResult(graph, seqPath):
    seqPath = np.array(seqPath)
    indices = np.where(graph == 1)
    rows = indices[0]
    columns = indices[1]
    
    printedDouble = []
    
    finalString = ""
    
    f = open("answer3.3.10.txt","w+")

    for i in range(0,len(rows)):
        col = columns[i]
        row = rows[i]

        if len(np.where(rows == row)[0]) == 1:
            finalString += seqPath[row] + ' -> ' + seqPath[col] + '\n'
        else:
            if seqPath[row] not in printedDouble:
                s = seqPath[row] + ' -> ' + seqPath[col]
                for ii in range(1,len(np.where(rows == row)[0])):
                    s += ", " + seqPath[col+ii]
                finalString += s + '\n'
                printedDouble.append(seqPath[row])

    f.write(finalString)
    return finalString
    
f = open("/Users/denniskenbeek/Downloads/dataset_327608_10.txt", "r")
seqPath = f.read().split('\n')
f.close()
k = len(seqPath[0]) 

print(OverlapGraph(seqPath, k))

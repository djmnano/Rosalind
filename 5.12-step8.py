#5.12: Code Challenge: Solve the Alignment with Affine Gap Penalties Problem.

import numpy as np

#made by dennis kenbeek (4686357)

def MakeMatrices(scores):
    scoreRef = scores[0]
    scoreRef = scoreRef.split(' ')
    filter_object = filter(lambda x: x != "", scoreRef)
    scoreRef = np.asarray(list(filter_object))
    
    scoreMatrix = np.zeros((len(scoreRef),len(scoreRef)),)
    
    for i in range(0, len(scoreMatrix)):
        row = list(filter(lambda x: x != "", scores[i+1].split(' ')[1:]))
        scoreMatrix[i][:] = row
    
    return scoreMatrix, scoreRef

def BackTrack(matrix, backtr_lower, backtr_upper, backtr_middle, v, w,  v_list, w_list, i,j):
    if i <= 0 or j <= 0:
        return
    if matrix == 0: #we are in lower
        if backtr_lower[i][j] == 1: #go to middle
            matrix = 1
        BackTrack(matrix, backtr_lower, backtr_upper, backtr_middle, v, w,  v_list, w_list, i-1,j)
        w_list.append('-')
        v_list.append(v[i-1])
            
    elif matrix == 1: #middle
        if backtr_middle[i][j] == 0: #go to lower
            matrix = 0
            BackTrack(matrix, backtr_lower, backtr_upper, backtr_middle, v, w,  v_list, w_list, i,j)
        elif backtr_middle[i][j] == 2: #go to upper
            matrix = 2
            BackTrack(matrix, backtr_lower, backtr_upper, backtr_middle, v, w,  v_list, w_list, i,j)
        else:
            BackTrack(matrix, backtr_lower, backtr_upper, backtr_middle, v, w,  v_list, w_list, i-1,j-1)
            w_list.append(w[j-1])
            v_list.append(v[i-1])
            
    else: #upper
        if backtr_upper[i][j] == 1: #go to middle
            matrix = 1
        
        BackTrack(matrix, backtr_lower, backtr_upper, backtr_middle, v, w,  v_list, w_list, i,j-1)
        v_list.append('-')
        w_list.append(w[j-1])

def FittingAlignment(v, w, sigma, epsilon, scoreMatrix, scoreRef):
    n = len(v)
    m = len(w)
    
    lower = np.zeros((n+1,m+1), dtype=int)
    upper = np.zeros((n+1,m+1), dtype=int)
    middle = np.zeros((n+1,m+1), dtype=int)

    backtr_lower = np.zeros((n+1,m+1), dtype=int)
    backtr_upper = np.zeros((n+1,m+1), dtype=int)
    backtr_middle = np.zeros((n+1,m+1), dtype=int)
    
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            
            v_pos = np.where(scoreRef == v[i-1])[0][0]
            w_pos = np.where(scoreRef == w[j-1])[0][0]
            
            lower_scores = [lower[i-1][j]-epsilon, middle[i-1][j]-sigma]
            lower[i][j] = max(lower_scores)
            backtr_lower[i][j] = lower_scores.index(lower[i][j])
            
            upper_scores = [upper[i][j-1]-epsilon, middle[i][j-1]-sigma]
            upper[i][j] = max(upper_scores)
            backtr_upper[i][j] = upper_scores.index(upper[i][j])
            
            middle_scores = [lower[i][j], middle[i-1][j-1] + scoreMatrix[v_pos][w_pos], upper[i][j]]
            middle[i][j] = max(middle_scores)
            backtr_middle[i][j] = middle_scores.index(middle[i][j])
    
    #find backtrack matrix to start with
    finalValues = [backtr_lower[n][m],backtr_middle[n][m],backtr_upper[n][m]]
    matrix = finalValues.index(max(finalValues))
  
    v_list = []
    w_list = []
    
    BackTrack(matrix, backtr_lower, backtr_upper, backtr_middle, v, w,  v_list, w_list, n,m)
    
    print(middle[n][m])
    
    v_list_2 = v_list[:-2] 
    v_list_2.append(v_list[-1])
    w_list = w_list[:-1] 
    
    print(*v_list_2,sep='')
    print(*w_list,sep='')
    
    return 
    
f = open("/Users/denniskenbeek/Downloads/dataset_327660_8.txt", "r")
data = f.read().split('\n')
f.close()

f = open("/Users/denniskenbeek/Downloads/BLOSUM62.txt", "r")
BLOSUM62 = f.read().split('\n')
f.close()

sigma = 11
epsilon = 1

v = data[0]
w = data[1]

scoreMatrix, scoreRef = MakeMatrices(BLOSUM62)

FittingAlignment(v, w, sigma, epsilon, scoreMatrix, scoreRef)

#1.8 Code Challenge: Solve the Frequent Words with Mismatches Problem.

#Made by Dennis Kenbeek (4686357)

def HammingDistance(seq1, seq2):
    d = 0
    for i in range(0,len(seq1)):
        if seq1[i] != seq2[i]:
            d += 1
    return d

def Neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return ['A', 'T', 'C', 'G']
    neighborhood = {}
    suffixNeighborhood = Neighbors(pattern[1:], d)
    for x in suffixNeighborhood:
        if HammingDistance(x,pattern[1:]) < d:
            nts = ['A', 'T', 'C', 'G']
            for y in nts:
                neighborhood[y+x] = 1    
        else:
            neighborhood[pattern[0]+x] = 1
    return neighborhood
    
            
def ApproximatePatternCount(seq, k, d):
    freqTable = {}
    for i in range(0,len(seq)-k+1):
        pattern = seq[i:i+k]
        neighbors = Neighbors(pattern, d)
        for x in neighbors:
            if x not in freqTable:
                freqTable[x] = 1
            else:
                freqTable[x] = freqTable[x] + 1
    return freqTable

def MaxMap(kmer_dict):
    max_values = max(kmer_dict.values())
    max_keys = [x for x, v in kmer_dict.items() if v == max_values]
    
    print(*max_keys, sep=' ')
    return

f = open("/Users/denniskenbeek/Downloads/dataset_327579_9.txt", "r")
data = f.read().split('\n')
f.close()

seq = data[0]
k = int(data[1].split(' ')[0])
d = int(data[1].split(' ')[1])

MaxMap(ApproximatePatternCount(seq,k,d))

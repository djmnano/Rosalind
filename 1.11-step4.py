
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

f = open("/Users/denniskenbeek/Downloads/dataset_327582_4.txt", "r")
data = f.read().split('\n')
f.close()

seq = data[0]
d = int(data[1])

print(*Neighbors(seq, d), sep=' ')

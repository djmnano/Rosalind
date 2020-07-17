#1.8 Code Challenge: Solve the Approximate Pattern Matching Problem.

#Made by Dennis Kenbeek (4686357)

def HammingDistance(seq1, seq2):
    d = 0
    for i in range(0,len(seq1)):
        if seq1[i] != seq2[i]:
            d += 1
    return d

def FindPatterns(seq, pattern, d):
    pos = []
    for i in range(0,len(seq)-len(pattern)+1):
        if HammingDistance(seq[i:i+len(pattern)], pattern) <= d:
            pos.append(i)
    return pos

f = open("/Users/denniskenbeek/Downloads/dataset_327579_4.txt", "r")
data = f.read().split('\n')
f.close()

pattern = data[0]
seq = data[1]
d = int(data[2])
print(*FindPatterns(seq,pattern,d),sep=' ')

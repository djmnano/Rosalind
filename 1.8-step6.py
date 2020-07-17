#1.8 Code Challenge: Implement ApproximatePatternCount

#Made by Dennis Kenbeek (4686357)

def HammingDistance(seq1, seq2):
    d = 0
    for i in range(0,len(seq1)):
        if seq1[i] != seq2[i]:
            d += 1
    return d

def ApproximatePatternCount(seq, pattern, d):
    c = 0
    for i in range(0,len(seq)-len(pattern)+1):
        if HammingDistance(seq[i:i+len(pattern)], pattern) <= d:
            c += 1
    return c

f = open("/Users/denniskenbeek/Downloads/dataset_327579_6.txt", "r")
data = f.read().split('\n')
f.close()

pattern = data[0]
seq = data[1]
d = int(data[2])

print(ApproximatePatternCount(seq,pattern,d))

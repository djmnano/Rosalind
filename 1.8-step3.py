#hamming distance

#Made by Dennis Kenbeek (4686357)

def HammingDistance(seq1, seq2):
    d = 0
    for i in range(0,len(seq1)):
        if seq1[i] != seq2[i]:
            d += 1
    return d

f = open("/Users/denniskenbeek/Downloads/dataset_327579_3.txt", "r")
data = f.read().split('\n')
f.close()

seq1 = data[0]
seq2 = data[1]

print(HammingDistance(seq1, seq2))         

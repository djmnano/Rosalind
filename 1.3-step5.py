#1.3 Code Challenge: Solve the Pattern Matching Problem. -> applied on V. cholerae genome

#Made by Dennis Kenbeek (4686357)

def PatternMatching(dna,pattern):
    pos = []
    for i in range(0,len(dna)-len(pattern)+1):
        if dna[i:i+len(pattern)] == pattern:
            pos.append(i)
    print(*pos, sep=' ')

f = open("/Users/denniskenbeek/Downloads/dataset_327574_5.txt", "r")
data = f.read().split('\n')
f.close()

if ' ' in data:
    data.remove(' ')

dna = data[1]
pattern = data[0]

PatternMatching(dna,pattern)

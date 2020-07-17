#1.3 Code Challenge: Solve the Reverse Complement Problem.

#Made by Dennis Kenbeek (4686357)

def revComplement(dna):
    c_dna = ''
    for i in range(len(dna)-1,-1,-1): #go backwards
        if dna[i] == 'A':
            c_dna += 'T'
        elif dna[i] == 'G':
            c_dna += 'C'
        elif dna[i] == 'T':
            c_dna += 'A'
        elif dna[i] == 'C':
            c_dna += 'G'
    return(c_dna)

f = open("/Users/denniskenbeek/Downloads/dataset_327574_2.txt", "r")
data = f.read().split('\n')
f.close()

if ' ' in data:
    data.remove(' ')

dna = data[0]

print(revComplement(dna))

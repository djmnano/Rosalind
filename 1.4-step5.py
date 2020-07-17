#question on clumps -> making it more efficient

#Made by Dennis Kenbeek (4686357)

def Clumps(seq, k, L, t):
    dict_pos = {}
    
    clumps = []
    for i in range(0, len(seq)-k+1):
        kmer = seq[i:i+k]  #get the kmer
        print(kmer)
        if kmer in dict_pos:
            dict_pos[kmer] = dict_pos[kmer] + [i]
            pos_array = dict_pos[kmer]
            if len(pos_array) >= t: #check whether this kmer appeared t times
                if (pos_array[-1]+k) - pos_array[0] <= L: #check whether this was in a window of L length
                    if kmer not in clumps:
                        clumps.append(kmer)
                else: #otherwise we remove the first one
                    dict_pos[kmer] = pos_array[1:len(pos_array)]           
        else:
            dict_pos[kmer] = [i]

    return clumps

f = open("/Users/denniskenbeek/Downloads/dataset_327575_5.txt", "r")
data = f.read().split('\n')
f.close()

if ' ' in data:
    data.remove(' ')

dna = data[0]

s = data[1].split(' ')
k = int(s[0])
L = int(s[1])
t = int(s[2])

print(*Clumps(dna, k, L, t), sep=' ')

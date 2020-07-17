#1.2 Hidden Messages in the replication origin; Code Challenge: Solve the frequent words problem

#Made by Dennis Kenbeek (4686357)

def BetterFrequentWords(text, k):
    kmer_dict = {}
    for i in range(0,len(text)-k+1):
        kmer = text[i:i+k]
        if kmer in kmer_dict: #if kmer is in dictionary, count it
            kmer_dict[kmer] = kmer_dict[kmer] + 1
        else: #else add it to the dictionary
            kmer_dict[text[i:i+k]] = 1
    MaxMap(kmer_dict)        
    return

def MaxMap(kmer_dict):
    max_values = max(kmer_dict.values()) #get the max value from the dictionary
    max_keys = [x for x, v in kmer_dict.items() if v == max_values] #give all the keys that have the max value
    
    print(*max_keys, sep=' ')
    return

f = open("/Users/denniskenbeek/Downloads/dataset_327573_13.txt", "r")
data = f.read().split('\n')
f.close()

if ' ' in data:
    data.remove(' ')

text = data[0]
k = int(data[1])

BetterFrequentWords(text,k)

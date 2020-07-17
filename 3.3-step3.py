#3.3 code challenge: solve the string spelled by a genome path problem

# made by dennis kenbeek (4686357)

def StringFromGenomePath(seqPath):
    seq = seqPath[0]

    for i in range(1,len(seqPath)-1):
        seq += seqPath[i][-1]
    return seq
f = open("/Users/denniskenbeek/Downloads/dataset_327608_3.txt", "r")

seqPath = f.read().split('\n')

f.close()
print(StringFromGenomePath(seqPath))

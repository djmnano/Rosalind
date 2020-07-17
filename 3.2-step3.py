#made by dennis kenbeek (4686357)

def Composition(s,k):
    composition = []
    for i in range(len(s)-k+1):
        composition += [s[i:i+k]]
    return composition


f = open("/Users/denniskenbeek/Downloads/dataset_327607_3.txt", "r")
data = f.read().split('\n')
f.close()

seq = data[1]
k = int(data[0])
comp = Composition(seq,k)

f = open("answer3.2.txt","w+")

for x in comp:
    f.write(x + '\n')
f.close()

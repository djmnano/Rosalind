#1.7 Code challenge: solve the minimumskew problem

#Made by Dennis Kenbeek (4686357)

def FindMinSkew(seq):
    skew = [0]

    for i in range(0,len(seq)):
        if seq[i] == 'C':
            x = -1
        elif seq[i] == 'G':
            x = 1
        else:
            x = 0
        skew.append(skew[i]+x)

    pos = []
    m = min(skew)
    for i in range(len(skew)):
        if skew[i] == m  and i not in pos:
            pos.append(i)
    
    print(*pos, sep=' ')


f = open("/Users/denniskenbeek/Downloads/dataset_327578_6.txt", "r")
data = f.read().split('\n')
f.close()

if ' ' in data:
    data.remove(' ')

FindMinSkew(data[0])

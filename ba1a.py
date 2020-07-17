#1.2 Hidden Messages in the replication origin; Code Challenge: Implement PatternCount

#Made by Dennis Kenbeek (4686357)

def PatternCount(text, pattern):
    counter = 0
    for i in range(0,len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            counter = counter + 1
    print(counter)
    return

f = open("/Users/denniskenbeek/Downloads/dataset_327573_6.txt", "r")
data = f.read().split('\n')
f.close()

if ' ' in data:
    data.remove(' ')

text = data[0]
pattern = data[1]

PatternCount(text,pattern)

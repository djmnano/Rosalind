#1.2 Hidden Messages in the replication origin; Code Challenge: Implement PatternCount

#Made by Dennis Kenbeek

def PatternCount(text, pattern):
    counter = 0
    for i in range(0,len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            counter = counter + 1
    print(counter)
    return

f = open("path", "r")
data = f.read().split('\n')
f.close()

if ' ' in data:
    data.remove(' ')

text = data[0]
pattern = data[1]

PatternCount(text,pattern)

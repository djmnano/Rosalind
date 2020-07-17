#5.5: Code Challenge: Solve the Change Problem.

#made by dennis kenbeek (4686357)

def DPChange(money, coins):
    MinNumCoins = {0:0}
    for m in range(1,money+1):
        MinNumCoins[m] = 10000000000
        for i in range(0,len(coins)):
            if m >= coins[i]:
                if MinNumCoins[m-coins[i]] + 1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m-coins[i]] + 1
 
    return MinNumCoins[money]

f = open("/Users/denniskenbeek/Downloads/dataset_327653_10.txt", "r")
data = f.read().split('\n')
f.close()

money = int(data[0])
coins = data[1].split(',')
coins = list(map(int,coins))
print(DPChange(money, coins))

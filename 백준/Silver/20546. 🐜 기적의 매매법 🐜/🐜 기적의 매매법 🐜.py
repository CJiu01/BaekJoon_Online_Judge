import sys
input = sys.stdin.readline

def jun(money):
    cnt = 0
    
    for i in stock:
        cnt += (money//i)
        money -= (money//i)*i
        
    return asset(money, cnt)

def sung(money):
    cnt = 0
    rising = 0
    falling = 0
    
    for i in range(len(stock)-1):
        if stock[i] < stock[i+1]:
            rising += 1
            falling = 0
        elif stock[i] > stock[i+1]:
            falling += 1
            rising = 0
        
        if rising == 3:
            money += (cnt*stock[i+1])
            cnt = 0
            rising = 0

        elif falling == 3:
            cnt += (money//stock[i+1])
            money -= (money//stock[i+1])*stock[i+1]
            falling = 0

    return asset(money, cnt)
    
def asset(money, stock_count):
    whole_asset = money + stock[13]*stock_count
    return whole_asset

money = int(input())
stock = list(map(int,input().split()))

jun_asset = jun(money)
sung_asset = sung(money)
if jun_asset > sung_asset:
    print("BNP")
elif jun_asset < sung_asset:
    print("TIMING")
else:
    print("SAMESAME")



# v2
M = int(input())
data = [[M,0],[M,0]]
D = list(map(int, input().split()))

for i in range(14):
    t1 = data[0][0]//D[i]
    data[0][0] -= (t1 * D[i]) 
    data[0][1] += t1
    
    if i<3:
        continue
    elif D[i-3] < D[i-2] < D[i-1] < D[i]:
        # 팔자
        data[1][0] += data[1][1] * D[i]
        data[1][1] = 0
    elif D[i-3] > D[i-2] > D[i-1] > D[i]:
        # 사자
        t2 = data[1][0] // D[i]
        data[1][0] -= D[i]*t2
        data[1][1] += t2

BNP = data[0][0] + data[0][1]*D[-1]
TIMING = data[1][0] + data[1][1]*D[-1]

if BNP > TIMING:
    print("BNP")
elif BNP < TIMING:
    print("TIMING")
else:
    print("SAMESAME")

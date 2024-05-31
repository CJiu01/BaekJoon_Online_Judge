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

import sys
input = sys.stdin.readline

t = int(input())

max = 10001
dp = [0]*max
dp[0] = 1

for coin in [1,2,3]:
    for i in range(coin,max):
        dp[i] += dp[i-coin]
        
for _ in range(t):
    n = int(input())
    print(dp[n])
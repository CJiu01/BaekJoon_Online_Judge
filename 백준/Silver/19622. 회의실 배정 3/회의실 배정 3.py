import sys
input = sys.stdin.readline

def conference(dp):
    dp[0] = arr[0][2]
    if(N<=1):
        return 
    
    dp[1] = max(dp[0],arr[1][2])
    for i in range(2,N):
        dp[i] = max(dp[i-1], dp[i-2]+arr[i][2])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0]*N

conference(dp)
print(max(dp))
import sys
input = sys.stdin.readline
import copy

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = copy.deepcopy(arr)

for i in range(N):
    for j in range(N):
        if (i==0 and j==0):
            continue
        elif (i==0):
            dp[i][j] += dp[i][j-1]
        elif (j==0):
            dp[i][j] += dp[i-1][j]
        else:
            dp[i][j] += dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(M):     
    x1, y1, x2, y2 = [int(x)-1 for x in input().split()]
          
    if (x1==0 and y1==0):
        res = dp[x2][y2]
    elif (x1==0):
        res = dp[x2][y2]-dp[x2][y1-1]
    elif (y1==0):
        res = dp[x2][y2]-dp[x1-1][y2]
    else:
        res = dp[x2][y2]-dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
        
    print(res)
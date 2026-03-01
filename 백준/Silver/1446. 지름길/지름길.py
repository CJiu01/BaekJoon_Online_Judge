N, D = map(int, input().split())
shortcut = [[] for _ in range(D+1)]

for i in range(N):
    start, end, cost = map(int, input().split())
    if start<=D:
        shortcut[start].append((end, cost))
    
dp = [float('inf')]*(D+1)
dp[0] = 0

for i in range(D+1):
    if i>0:
        dp[i] = min(dp[i],dp[i-1]+1)
        
    for end, cost in shortcut[i]:
        if end<=D:
            dp[end] = min(dp[end], dp[i]+cost)
        
print(dp[D])
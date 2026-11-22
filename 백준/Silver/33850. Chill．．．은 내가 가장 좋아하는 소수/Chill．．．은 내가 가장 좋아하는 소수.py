def score(v):
    for i in range(2, int(v**0.5)+1):
        if v%i==0:
            return b
    return a

def solution(n,l):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = score((l[0][1] + l[1][1]))
    
    for i in range(2,n+1):
        ver = dp[i-2] + score(l[0][i-1]+l[0][i]) + score(l[1][i-1]+l[1][i])
        hor = dp[i-1] + score(l[0][i]+l[1][i])
        dp[i] = max(ver, hor)

    return dp[n]

global a,b
n, a, b = map(int, input().split())
l = []
for _ in range(2):
    l.append([0]+list(map(int, input().split())))
print(solution(n,l))
import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

n = len(S)
m = len(T)

dp = [0] * (m + 1)
res = 0

for i in range(1, n + 1):
    for j in range(m, 0, -1): 
        if S[i - 1] == T[j - 1]:
            dp[j] = dp[j - 1] + 1
            res = max(res, dp[j])
        else:
            dp[j] = 0

print(res)
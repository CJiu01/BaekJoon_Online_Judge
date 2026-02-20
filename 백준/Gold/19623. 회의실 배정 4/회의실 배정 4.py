import sys
import bisect

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    s, e, p = map(int, input().split())
    arr.append((s, e, p))

arr.sort(key=lambda x: x[1])
ends = [arr[i][1] for i in range(n)]

dp = [0] * n
dp[0] = arr[0][2]

for i in range(1, n):
    s, e, p = arr[i]
    idx = bisect.bisect_left(ends, s) - 1

    include = p
    if idx >= 0:
        include += dp[idx]

    dp[i] = max(dp[i - 1], include)

print(dp[n - 1])
def solution(x, y, n):
    answer = 0
    max_value = 10**9
    dp = [max_value]*(y+1)
    dp[y] = 0
    
    for i in range(y,x,-1):
        if dp[i] == max_value:
            continue
        if i%2==0:
            dp[i//2] = min(dp[i//2], dp[i]+1)
        if i%3==0:
            dp[i//3] = min(dp[i//3], dp[i]+1) 
        if i-n>=x:
            dp[i-n] = min(dp[i-n], dp[i]+1)

    return dp[x] if dp[x]!=max_value else -1

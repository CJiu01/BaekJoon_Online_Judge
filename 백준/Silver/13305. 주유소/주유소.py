def solution(n,length, price):
    cur = price[0]
    res = 0
    
    for i in range(n-1):
        cur = min(cur, price[i])    
        res += cur*length[i]   
    return res

n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))
print(solution(n,length, price))
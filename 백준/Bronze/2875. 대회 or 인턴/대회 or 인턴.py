n, m, k = map(int, input().split())

count = 0
while n+m>=3+k:
    if n-2>=0 and m-1>=0:
        count+=1
        n -= 2
        m -= 1
    else:
        break
    
print(count)
N,K = map(int, input().split())
arr = list(map(int, input().split()))
same = [0]*100001

start = 0
res = 0

for end in range(N):
    same[arr[end]] += 1
    
    while (same[arr[end]]>K):
        same[arr[start]] -= 1
        start += 1
        
    res = max(res, end-start+1)
    
print(res)
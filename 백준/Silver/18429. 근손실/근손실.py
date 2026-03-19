from itertools import permutations

def check(p,k,kit):
    weight=500
    
    for i in p:
        tmp = weight-k+kit[i]
        if tmp<500:
            return False
        weight = tmp
    
    return True

N, K = map(int, input().split())
kit = list(map(int, input().split()))
permu = list(permutations([i for i in range(N)], N))
ans = 0
for p in permu:
    if check(p,K,kit):
        ans += 1
        
print(ans)
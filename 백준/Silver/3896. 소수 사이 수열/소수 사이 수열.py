prime = [True] * (1299709+1)

for i in range(2,(1299709+1)):
    if not prime[i]:
        continue
    for j in range(i+i, (1299709+1), i):
        prime[j]=False

n = int(input())
for _ in range(n):
    k = int(input())
    
    if prime[k]:
        print(0)
        continue
    
    left = k-1
    right = k+1
    while True:
        if prime[left]:
            break
        left -= 1
        
    while True:
        if prime[right]:
            break
        right += 1
    
    print(right-left)
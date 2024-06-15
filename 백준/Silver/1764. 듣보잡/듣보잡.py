from collections import Counter

N, M = map(int, input().split())
A, B = [], []
for _ in range(N+M):
    A.append(input())
    
A = Counter(A)
cnt = 0
for i in A:
    if A[i]>1:
        B.append(i)
        cnt += 1
B.sort()
print(cnt)
print(*B, sep='\n')
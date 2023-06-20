N, M = map(int, input().split())
A, B = [], []

for row in range(N):
    li = list(map(int, input().split()))
    A.append(li)
    
for row in range(N):
    li = list(map(int, input().split()))
    B.append(li)

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print()
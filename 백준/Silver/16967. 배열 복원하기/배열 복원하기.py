H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H+X)]
A = []

for i in range(H):
    A.append(B[i][:W])

for i in range(X,H):
    for j in range(Y,W):
        A[i][j] -= A[i-X][j-Y]

for i in A:     
    print(*i)
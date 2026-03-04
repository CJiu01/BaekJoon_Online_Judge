from itertools import product

moves = [[[(0,1)], [(1,0)], [(0,-1)], [(-1,0)]], [[(0,-1),(0,1)], [(-1,0),(1,0)]], [[(-1,0),(0,1)], [(0,-1),(-1,0)] , [(0,-1),(1,0)], [(0,1),(1,0)]], [[(0,-1),(0,1),(-1,0)], [(0,-1),(0,1),(1,0)],[(-1,0),(1,0),(0,-1)], [(-1,0),(1,0),(0,1)]], [[(-1,0),(0,1),(0,-1),(1,0)]]] 

monitors = []

def cctv(x,y):
    cases = []

    for move in moves[graph[x][y]-1]:
        monitor = [[False]*M for _ in range(N)]

        for m in move:
            dx, dy = x,y
                
            while True:
                dx += m[0]
                dy += m[1]

                if not (0 <= dx < N and 0 <= dy < M):
                    break
                if graph[dx][dy] == 6:
                    break

                monitor[dx][dy] = True
                
        cases.append(monitor)
        
    return cases

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if 1<=graph[i][j]<=5:
            monitors.append(cctv(i,j))
    
ans = float('inf')
for case in product(*monitors):
    
    total = [[False]*M for _ in range(N)]

    for m in case:
        for i in range(N):
            for j in range(M):
                if m[i][j]:
                    total[i][j] = True

    # 사각지대 계산
    blind = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0 and not total[i][j]:
                blind += 1

    ans = min(ans, blind)
print(ans)
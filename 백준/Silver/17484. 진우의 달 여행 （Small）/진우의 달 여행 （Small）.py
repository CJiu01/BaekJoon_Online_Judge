def space(dir, gas, x, y):
    if(x==N-1):
        res.append(gas)
        return 
        
    for i in range(3):
        if dir==i:
            continue
        dx = x+move[i][0]
        dy = y+move[i][1]
        if(0<=dx<N and 0<=dy<M):
            space(i, gas+graph[dx][dy], dx, dy)
    return 

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = int(1e9)
res = []

move = [[1,-1],[1,0],[1,1]]
for i in range(M):
    space(-1, graph[0][i], 0, i)

print(min(res))
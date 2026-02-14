from collections import deque
import copy

def floodedplace(N, flooded, height):
    for i in range(N):
        for j in range(N):
            if (flooded[i][j]<=height):
                flooded[i][j] = 0
            else:
                flooded[i][j] = 1
                

def bfs(x, y, flooded, visited):
    dx = [0,0,-1,1]
    dy = [-1, 1, 0, 0]
    
    queue = deque([(x,y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if (0<=nx<N and 0<=ny<N):
                if (flooded[nx][ny]==1 and (not visited[nx][ny])):
                    queue.append((nx,ny))
                    visited[nx][ny] = True

N = int(input())
graph = []
height = set()

for i in range(N):
    l = list(map(int, input().split()))
    graph.append(l)
    height.update(l)

res = 1
for i in height:
    flooded = copy.deepcopy(graph)
    floodedplace(N, flooded, i)
    
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if (flooded[i][j]==1 and (not visited[i][j])):
                bfs(i,j, flooded, visited)
                cnt += 1
    res = max(res, cnt)

print(res)
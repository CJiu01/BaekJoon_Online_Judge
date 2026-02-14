from collections import deque            

def bfs(x, y, graph, visited,h):
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
                if (graph[nx][ny]>h and (not visited[nx][ny])):
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
for h in height:
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if (graph[i][j]>h and (not visited[i][j])):
                bfs(i,j, graph, visited, h)
                cnt += 1
    res = max(res, cnt)

print(res)
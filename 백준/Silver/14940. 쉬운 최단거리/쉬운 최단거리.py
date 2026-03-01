from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = 0
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 0

                elif graph[nx][ny] == 1 and visited[nx][ny] == -1:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y]+1

    
    
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

x, y = -1,-1
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            x,y=i,j
        elif graph[i][j]==0:
            visited[i][j]=0


bfs(x,y)
for i in range(n):
    print(*visited[i])
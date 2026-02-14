from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(graph, visited, i, j):
    queue = deque([(i,j)])
    visited[i][j] = True
    cnt = 1
    while queue:
        x, y = queue.popleft()
        
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            
            if (0<=nx and nx<N and 0<=ny and ny<M):
                if (graph[nx][ny]==0 and (not visited[nx][ny])):
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
    return cnt
    
M, N, K = map(int, input().split())
graph = [[0]*M for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

visited = [[False]*M for _ in range(N)]   
width = [] 
for i in range(N):
    for j in range(M):
        if (graph[i][j]==0 and not visited[i][j]):
            width.append(bfs(graph, visited, i, j))


print(len(width))
print(' '.join(map(str, sorted(width))))
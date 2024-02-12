from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx>=0 and ny>=0 and nx<n and ny<m:
                if graph[nx][ny] == -1:
                    continue
                elif graph[nx][ny] ==0 or graph[nx][ny] > graph[x][y] + 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))
    return
        

m, n = map(int, input().split())
graph = [[]*m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

queue = deque(())
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))

bfs()      

res = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print("-1")
            sys.exit()
        res = max(res, graph[i][j])

print(res-1)
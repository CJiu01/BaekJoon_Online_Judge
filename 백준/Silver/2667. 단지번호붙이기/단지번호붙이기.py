import sys
from collections import deque

n = int(input())

graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = deque(())
    queue.append((x, y))
    graph[x][y] = 0
    count = 0
    
    while queue:
        x, y = queue.popleft()
        count += 1
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx>=0 and ny>=0 and nx<n and ny<n:
                if graph[nx][ny] == 1:
                    queue.append((nx,ny))
                    graph[nx][ny] = 0

    return count

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            result.append(bfs(i,j))
result.sort()    
print(len(result))
for i in result:
    print(i)
# breath first search: bfs
from collections import deque
import sys
input = sys.stdin.readline

# R(빨강), G(초록), B(파랑) 

di = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs_first(i,j,visited):
    queue = deque(())
    queue.append([i,j])
    visited[i][j] = True
    
    while queue:
        x, y =queue.popleft()
        
        for i in range(4):
            dx, dy = x+di[i][0], y+di[i][1]
            if 0<=dx<n and 0<=dy<n:
                if visited[dx][dy] == False and graph[dx][dy]==graph[x][y]:
                    queue.append([dx,dy])
                    visited[dx][dy] = True
    
    
n = int(input())
graph = []

for _ in range(n):
    graph.append(list(input().strip()))
    
visited = [[False]*n for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs_first(i,j,visited)
            count+=1
print(count,end=' ')



visited = [[False]*n for _ in range(n)]
count = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
                
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs_first(i,j,visited)
            count+=1
print(count)
 
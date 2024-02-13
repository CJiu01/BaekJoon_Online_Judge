import sys
from collections import deque
input = sys.stdin.readline

di = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(x,y):
    queue = deque(())
    queue.append([x,y])

    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx, ny = x+di[i][0], y+di[i][1]
            
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append([nx, ny])

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))
bfs(0,0)
print(graph[n-1][m-1])
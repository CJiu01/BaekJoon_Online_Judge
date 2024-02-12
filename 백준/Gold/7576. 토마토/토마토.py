from collections import deque
import sys
input = sys.stdin.readline

di = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs():
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            col, row = x+di[i][0], y+di[i][1]
            
            if 0<=col<n and 0<=row<m:
                if graph[col][row] == 0:
                    graph[col][row] = graph[x][y] + 1
                    queue.append([col,row])
        
m, n = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

queue = deque(())
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i,j])

bfs()      

res = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print("-1")
            sys.exit()
        res = max(res, graph[i][j])

print(res-1)
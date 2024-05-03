import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dir = [[-2,-1], [-1,-2], [-2,1], [-1,2], [1,-2], [2,-1], [2,1], [1,2]]


def bfs(start, graph, visited, size):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            
            if 0<=nx<size and 0<=ny<size:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append([nx,ny])
                    
                    graph[nx][ny] = graph[x][y] + 1

for i in range(n):
    size = int(input())
    st_x, st_y = map(int, input().split())
    en_x, en_y = map(int, input().split())
    
    graph = [[0 for _ in range(size)] for _ in range(size)]
    visited = [[False for _ in range(size)] for _ in range(size)]
    
    bfs((st_x, st_y), graph, visited, size)
    print(graph[en_x][en_y])
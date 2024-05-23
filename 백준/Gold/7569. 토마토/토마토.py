from collections import deque
import sys
input = sys.stdin.readline

dz = [0, 0, 0, 0, 1, -1]
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]

def bfs():
    global day
    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and graph[nz][nx][ny] == 0:
                queue.append((nz, nx, ny))
                graph[nz][nx][ny] = graph[z][x][y] + 1
                if day < graph[nz][nx][ny]:
                    day = graph[nz][nx][ny]-1


m, n, h = map(int, input().split())
graph = []
queue = deque([])

for z in range(h):
    graph1 = []
    for x in range(n):
        graph1.append(list(map(int, input().split())))
        for y in range(m):
            if graph1[x][y] == 1:
                queue.append((z, x, y))
    graph.append(graph1)

day = 0      
bfs()

for z in range(h):
    for x in range(n):
        if 0 in graph[z][x]:
            print(-1)
            exit()
        if z == h-1 and x == n-1:
            print(day)
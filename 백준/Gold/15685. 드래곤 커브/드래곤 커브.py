import sys
input = sys.stdin.readline

N = int(input())
graph = [[0]*101 for _ in range(101)]
dir = [[0,1],[-1,0],[0,-1],[1,0]]

for _ in range(N):
    y, x, d, g = map(int, input().split())
    graph[x][y] = 1
    
    # curve 리스트 생성
    curves = [d]
    for _ in range(g):
        for k in range(len(curves)-1,-1,-1):
            curves.append((curves[k]+1)%4)
            
    for curve in curves:
        x += dir[curve][0]
        y += dir[curve][1]
        if 0<=x<=100 and 0<=y<=100:
            graph[x][y] = 1

res = 0
for i in range(100):
    for j in range(100):
        if graph[i][j]==1 and graph[i+1][j]==1 and graph[i][j+1]==1 and graph[i+1][j+1]==1:
            res += 1
print(res)
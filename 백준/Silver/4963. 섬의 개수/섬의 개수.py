import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# dfs_ stack

def dfs(x,y):
    graph[x][y] = 0
    
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx>=0 and ny>=0 and nx<h and ny<w:
            if graph[nx][ny]==1: 
                dfs(nx,ny)
    return 
                
while True:
    w, h = map(int,input().split())
    
    if w==0 and h==0:
        break
    
    graph = [[0]*w for _ in range(h)]
    for i in range(h):
        graph[i] = list(map(int,input().split()))

    dx = [0,0,-1,1,-1,-1,1,1]
    dy = [-1,1,0,0,-1,1,-1,1]
    result = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                    dfs(i,j)
                    result += 1
    print(result)
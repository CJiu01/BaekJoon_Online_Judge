import copy


R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

up = [[0,1],[-1,0],[0,-1],[1,0]]
down = [[0,1],[1,0],[0,-1],[-1,0]]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def spread(x,y):
    amount = graph[x][y]//5
    cnt = 0
        
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0<=nx<R and 0<=ny<C):
            if new[nx][ny] != -1:
                new[nx][ny] += amount
                cnt += 1
    new[x][y] -= amount*cnt

def airconditioner(x,y,dir):
    rot[x][y] = 0
    for d in dir:
        while True:
            nx,ny = x+d[0], y+d[1]
            if not (0<=nx<R and 0<=ny<C):
                break
            elif new[nx][ny] == -1:
                return
            elif 0<=nx<R and 0<=ny<C:
                rot[nx][ny] = new[x][y]
                x, y = nx, ny
       
for _ in range(T):
    # spread        
    new = [row.copy() for row in graph]
    air_dir = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                spread(i,j)
            elif graph[i][j] == -1:
                air_dir.append([i,j])
    # rotate
    rot = [row.copy() for row in new]
    airconditioner(air_dir[0][0], air_dir[0][1]+1, up)
    airconditioner(air_dir[1][0], air_dir[1][1]+1, down)
    
    graph = [row.copy() for row in rot]  

ans = 2  
for r in graph:
    ans += sum(r)
    
print(ans)
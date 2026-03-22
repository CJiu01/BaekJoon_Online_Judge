from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dir = [(-1,0),(0,-1),(0,1),(1,0)]
x,y,size = 0,0,2
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            x,y = i,j

            
def solve(x,y,size):
    
    visited = [[False]*N for _ in range(N)]
    distance = [[0]*N for _ in range(N)]
    q = deque([(x,y)])
    visited[x][y] = True
    tmp = []
    
    while q:
        cur_x, cur_y = q.popleft()
        
        for i in range(4):
            dx = cur_x+dir[i][0]
            dy = cur_y+dir[i][1]
            
            if (0<=dx<N and 0<=dy<N) and not visited[dx][dy]:
                if graph[dx][dy]<=size:
                    visited[dx][dy] = True
                    distance[dx][dy] = distance[cur_x][cur_y]+1
                    q.append([dx,dy])

                    # 먹을 수 있다면
                    if 0<graph[dx][dy]<size:
                        tmp.append([dx,dy,distance[dx][dy]])
                    
    return sorted(tmp, key=lambda x: (-x[2],-x[0],-x[1]))


graph[x][y] = 0
fish_cnt = 0
ans = 0
while 1:
    fish = solve(x,y,size)
    
    if not fish:
        break
    
    nx,ny,dist = fish.pop()
    
    ans += dist
    graph[nx][ny] = 0
    x,y = nx,ny
    fish_cnt += 1
    
    if fish_cnt == size:
        size += 1
        fish_cnt = 0
        
print(ans)

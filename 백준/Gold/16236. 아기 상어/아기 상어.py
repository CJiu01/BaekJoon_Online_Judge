from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dir = [(-1,0),(0,-1),(0,1),(1,0)]
x,y,size = 0,0,2
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            x,y = i,j
            graph[x][y] = 0

            
def bite_fish(x,y,size):
    
    visited = [[False]*N for _ in range(N)]
    q = deque([(x,y,0)])
    visited[x][y] = True
    tmp = []
    prev_dist = 0
    
    while q:
        cur_x, cur_y, dist = q.popleft()
        
        if dist != prev_dist:
            if tmp:
                return tmp
            prev_dist = dist
        
        for i in range(4):
            dx = cur_x+dir[i][0]
            dy = cur_y+dir[i][1]
            
            if (0<=dx<N and 0<=dy<N) and not visited[dx][dy]:
                if graph[dx][dy]<=size:
                    visited[dx][dy] = True
                    q.append([dx,dy,dist+1])
                
                    # 먹을 수 있다면
                    if 0<graph[dx][dy]<size:
                        tmp.append([dx,dy, dist+1])
    return tmp  
    
fish_cnt = 0
ans = 0
while True:
    fish = bite_fish(x,y,size)
    
    if not fish:
        break
    
    fish.sort(key=lambda x:(-x[0],-x[1]))
    nx,ny,dist = fish.pop()
    
    ans += dist
    graph[nx][ny] = 0
    x,y = nx,ny
    fish_cnt += 1
    
    if fish_cnt == size:
        size += 1
        fish_cnt = 0
        
print(ans)
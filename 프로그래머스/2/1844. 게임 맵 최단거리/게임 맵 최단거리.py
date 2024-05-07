from collections import deque

def solution(maps):
    answer = 0
    queue = deque([(0, 0)])
    dir = [[0,1], [0,-1], [1,0], [-1,0]]
    n,m = len(maps), len(maps[0])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            dx, dy = x+dir[i][0], y+dir[i][1]
            
            if 0<=dx<n and 0<=dy<m:
                if maps[dx][dy] == 1:
                    maps[dx][dy] = maps[x][y] + 1
                    queue.append((dx,dy))
    
    if maps[n-1][m-1] > 1:
        answer = maps[n-1][m-1]
    else:
        answer = -1
    
    return answer


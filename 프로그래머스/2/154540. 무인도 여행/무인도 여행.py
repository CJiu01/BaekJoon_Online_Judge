from collections import deque

def bfs(x,y, maps,m,n):
    dir = [(0,1),(1,0),(-1,0),(0,-1)]
    q = deque([(x,y)])
    res = int(maps[x][y])
    maps[x][y] = 'X'

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            dx = x+dir[i][0]
            dy = y+dir[i][1]
            
            if 0<=dx<m and 0<=dy<n and maps[dx][dy]!='X':
                q.append((dx,dy))
                res += int(maps[dx][dy])
                maps[dx][dy] = 'X'
    return res

def solution(maps):
    answer = []
    m, n = len(maps), len(maps[0])
    maps = [list(i) for i in maps]
    
    for i in range(m):
        for j in range(n):
            if maps[i][j] != 'X':
                answer.append(bfs(i,j,maps,m,n))
    
    answer.sort()
    return answer if answer else [-1]
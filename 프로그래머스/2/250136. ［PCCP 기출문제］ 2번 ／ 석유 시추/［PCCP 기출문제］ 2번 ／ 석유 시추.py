from collections import deque

def bfs(land, x, y, res, n, m):
    
    q = deque([(x,y)])
    land[x][y] = 0
    s = set({y})
    cnt = 1
    dir = [[0,1],[1,0],[-1,0],[0,-1]]
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            dx = x + dir[i][0]
            dy = y + dir[i][1]
            
            if 0<=dx<n and 0<=dy<m:
                if land[dx][dy]==1:
                    q.append((dx,dy))
                    land[dx][dy] = 0
                    s.add(dy)
                    cnt+=1

    for v in s:
        res[v] += cnt
    return


def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    
    res = [0]*m
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                bfs(land, i, j, res, n, m)
    
    return max(res)
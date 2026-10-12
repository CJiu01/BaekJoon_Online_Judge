from collections import deque

def find_idx(maps, target, W,H):
    for i in range(H):
        if target in maps[i]:
            for j in range(W):
                if maps[i][j] == target:
                    return [i,j]

def bfs(target, maps, dist, x, y,W,H):
    q = deque([(x,y)])
    dist[x][y] = 0
    dir = [[0,1],[1,0],[0,-1],[-1,0]]
    
    while q:
        x,y =  q.popleft()
        
        for i in range(4):
            dx,dy = x+dir[i][0], y+dir[i][1]
            if 0<=dx<H and 0<=dy<W:
                
                if maps[dx][dy] != 'X' and dist[dx][dy]== -1:
                    q.append([dx,dy])
                    dist[dx][dy] = dist[x][y]+1
                
                if maps[dx][dy] == target:
                    return [dist[dx][dy],dx,dy]
    return [-1]
        

def solution(maps):
    answer = 0
    W,H = len(maps[0]), len(maps)
    
    # S->L
    x,y = find_idx(maps, 'S', W,H)
    dist = [[-1]*W for _ in range(H)]
    res = bfs('L', maps, dist, x,y,W,H)
    if res == [-1]:
        return -1
    answer += res[0]
    
    # L->E
    dist = [[-1]*W for _ in range(H)]
    res = bfs('E', maps, dist, res[1],res[2],W,H)
    if res == [-1]:
        return -1
    answer += res[0]
    
    return answer
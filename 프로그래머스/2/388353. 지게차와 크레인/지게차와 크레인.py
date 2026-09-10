from collections import deque

def solution(storage, requests):
    answer = 0
    n = len(storage)
    m = len(storage[0])
    storage = [list(i) for i in storage]
    dir = [[0,1],[1,0],[-1,0],[0,-1]]
    
    for req in requests:
        if len(req) == 1:
            
            visited = [[False]*m for _ in range(n)]
            q = deque()
            for i in range(n):
                q.append([i,0])
                q.append([i,m-1])
                visited[i][0] = True
                visited[i][m-1] = True

            for i in range(1,m-1):
                q.append([0,i])
                q.append([n-1,i])
                visited[0][i] = True
                visited[n-1][i] = True

            while q:
                x,y = q.popleft()
                if storage[x][y] == req:
                    storage[x][y] = ''
                elif storage[x][y] == '':
                    for i in range(4):
                        dx = x+dir[i][0]
                        dy = y+dir[i][1]
                        if 0<=dx<n and 0<=dy<m and not visited[dx][dy]:
                            if storage[dx][dy] == req:
                                storage[dx][dy] = ''
                                visited[dx][dy] = True
                            elif storage[dx][dy] == '':
                                q.append([dx,dy])
                                visited[dx][dy] = True
            
        else:
            t = req[0]
            for i in range(n):
                for j in range(m):
                    if storage[i][j]==t:
                        storage[i][j] = ''

    for i in storage:
        answer += i.count('')
    return (n*m - answer)
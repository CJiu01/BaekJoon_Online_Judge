def solution(n):
    answer = []
    
    dir = [(1,0),(0,1),(-1,-1)]
    l = [[-1]*n for _ in range(n)]
    x,y,d = 0,0,0
    v = 1
    
    l[0][0] = v
    v+=1
    for i in range(n,0,-1):
        k = d%3
        
        while True:
            dx = x+dir[k][0]
            dy = y+dir[k][1]
            
            if (not (0<=dx<n and 0<=dy<n)) or (l[dx][dy] != -1):
                break
            l[dx][dy] = v
            v+=1
            x,y = dx,dy
        d+=1
    
    for a in l:
        for b in a:
            if b==-1:
                continue
            answer.append(b)
    return answer
def solution(points, routes):
    answer = 0
    
    x = len(routes)
    p = len(routes[0])
    move = [[] for _ in range(x)]
    

    for i in range(x):
        move[i].append([points[routes[i][0]-1][0], points[routes[i][0]-1][1]])

        for j in range(p-1):
            start = points[routes[i][j]-1]
            end = points[routes[i][j+1]-1]
            
            # updown
            sign = 1 if start[0]<=end[0] else -1
            for k in range(start[0]+sign, end[0]+sign, sign):
                move[i].append([k,start[1]])
            
            # leftright
            sign = 1 if start[1]<=end[1] else -1
            for k in range(start[1]+sign, end[1]+sign, sign):
                move[i].append([end[0],k])
    
    n = (max([len(m) for m in move]))
    for i in range(n):
        arr = [[0]*101 for _ in range(101)]
        for j in range(x):
            if i>=len(move[j]):
                continue
            a,b = move[j][i][0], move[j][i][1]
            arr[a][b] +=1
            if arr[a][b] ==2:
                answer+=1
    
    return answer
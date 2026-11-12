def solution(arr):
    answer = []
    zero, one = 0,0
    
    point = [[0,0]]
    l = len(arr)
    n = l
    
    while n>1:
        diff = []
        for p in range(len(point)): 
            x,y = point[p][0],point[p][1]
            v = arr[x][y]
            flg = True
            
            for i in range(n):
                for j in range(n):
                    if v != arr[x+i][y+j]:
                        flg = False
                        break
                if not flg:
                    diff.append([x,y])
                    break
            
            if flg:
                if v == 0:
                    zero += 1
                else:
                    one += 1
                    
        n//=2
        new_p = []
        for p in diff:
            x,y = p[0],p[1]
            new_p.append([x,y])
            new_p.append([x,y+n])
            new_p.append([x+n,y])
            new_p.append([x+n,y+n])
        point = new_p[:]

    for p in point:
        if arr[p[0]][p[1]]:
            one += 1
        else:
            zero += 1
    
    return [zero, one]
def solution(routes):
    answer = 0
    left = 0
    routes.sort()
    
    while left<len(routes):
        
        c=routes[left][1]
        i = left+1
        while True:
            if i<len(routes) and routes[i][0] <= c:
                c=min(c,routes[i][1])
                i += 1
            else:
                break
        
        left = i
        answer += 1
    
    return answer
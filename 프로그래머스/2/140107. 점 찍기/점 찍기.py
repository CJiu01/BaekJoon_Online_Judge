def solution(k, d):
    answer = 0
    
    for i in range(1000001):
        if (k*i)**2 > d**2:
            break
        
        y = int((d**2 - (k*i)**2)**0.5)
        answer += (y//k + 1)
    
    return answer
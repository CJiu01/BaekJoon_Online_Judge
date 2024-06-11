def solution(n, lost, reserve):
    answer = 0
    cloth = [1]*(n+1)

    for i in range(len(lost)):
        cloth[lost[i]] -= 1
    
    for i in range(len(reserve)):
        cloth[reserve[i]] += 1
        
    for i in range(1,n+1):
        if cloth[i] == 0:
            if cloth[i-1] == 2:
                cloth[i-1] -= 1
                cloth[i] += 1
                answer += 1
            elif i<n and cloth[i+1] == 2:
                cloth[i+1] -= 1
                cloth[i] += 1
                answer += 1
        else:
            answer += 1
    
    return answer
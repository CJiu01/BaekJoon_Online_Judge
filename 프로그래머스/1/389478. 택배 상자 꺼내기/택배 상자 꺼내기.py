import math

def solution(n, w, num):
    stack = [[] for _ in range(w)]
    
    for i in range(1,n+1):
        if math.ceil(i/w)%2 == 0:
            stack[(w-(i%w))%w].append(i)
        else:
            stack[(i%w)-1].append(i)
        
    target = ((w-(num%w))%w) if math.ceil(num/w)%2==0 else (num%w)-1
    
    answer = 1
    while stack[target].pop() != num:
        answer += 1
    
    return answer
from collections import deque

def solution(players, m, k):
    answer = 0
    q = deque()
    
    for p in players:
        n = p//m
        f = q[0] if q else 0
        if n>f:
            tmp=deque()
            for i in range(k):
                v = q.popleft() if q else 0
                tmp.append(v+(n-f))
            q = tmp
            answer += (n-f)
        
        if q:
            q.popleft() 

    return answer

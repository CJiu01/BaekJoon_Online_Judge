from collections import deque

def solution(players, m, k):
    answer = 0
    q = deque()
    
    for p in players:
        n = p//m
        f = q[0] if q else 0
        if n>f:
            q = deque(
                (q.popleft() if q else 0) + (n-f)
                for _ in range(k)
            )
            answer += (n-f)
        if q:
            q.popleft() 

    return answer
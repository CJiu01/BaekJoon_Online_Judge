def solution(cards):
    answer = []
    n = len(cards)
    visited = [False]*(n)
    
    for i in range(n):
        v = i
        cnt = 0
        while not visited[v]:
            visited[v] = True
            v = cards[v]-1
            cnt += 1
        answer.append(cnt)
    
    answer.sort()
    return answer[-1]*answer[-2]
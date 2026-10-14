import heapq

def solution(n, k, enemy):
    answer = 0
    shield = []
    
    for i in enemy:
        if k>0:
            heapq.heappush(shield, i)
            k -= 1
            answer += 1
            continue
        
        h = heapq.heappop(shield)
        if h<i:
            if n-h<0:
                return answer
            heapq.heappush(shield, i)
            n -= h
        else:
            if n-i<0:
                return answer
            heapq.heappush(shield, h)
            n -= i
    
        answer += 1
        
    return answer
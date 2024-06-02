import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while any(K>num for num in scoville):
        a,b = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, mixed(a,b))
        answer += 1
        
        if len(scoville) == 1:
            if K > scoville[0]:
                return -1
            else:
                break
    
    return answer

def mixed(fir, sec):
    return fir + (sec*2)
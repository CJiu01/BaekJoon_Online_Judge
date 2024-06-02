from heapq import heapify, heappush, heappop
def solution(scoville, K):
    heapify(scoville)
    for i in range(1000000):
        try:
            if scoville[0] >= K: return i
            heappush(scoville, heappop(scoville)+(heappop(scoville)*2))
        except:
            return -1
from collections import deque
from collections import Counter

def bfs(numbers):
    queue = deque([-1*numbers[0], numbers[0]])
    
    for k in range(1,len(numbers)):
        tmp = []
        for i in queue:
            tmp.extend([i-numbers[k], i+numbers[k]])
        queue = tmp
            
    return queue

def solution(numbers, target):
    
    q = bfs(numbers)
    answer = Counter(q)[target]
    return answer
from collections import deque

def solution(queue1, queue2):
    answer = 0
    arr = queue1+queue2
    target_value = sum(arr)//2
    if target_value*2 != sum(arr):
        return -1
    
    i,j = 0, len(queue1)
    cur = sum(queue1)
    while i<j<len(arr):
        if cur==target_value:
            return answer
        elif cur > target_value:
            cur -= arr[i]
            i+=1
            answer += 1
        elif cur < target_value:
            cur += arr[j]
            j+=1
            answer+=1
    return -1
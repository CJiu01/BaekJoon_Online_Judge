def solution(sequence, k):
    left, cur = 0,0
    answer = []
    for right, x in enumerate(sequence):
        cur += x
        
        while cur>k:
            cur -= sequence[left]
            left += 1
        
        if cur == k:
            answer.append([right-left, left, right])
            
    answer.sort()
    return [answer[0][1], answer[0][2]]
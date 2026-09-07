def solution(elements):
    
    answer = set()
    n = len(elements)
    prev = [0]*n
    
    for i in range(n):
        curr = []
        for j in range(n):
            v = prev[j]+elements[(i+j)%n]
            curr.append(v)
            answer.add(v)
        prev = curr
    return len(answer)
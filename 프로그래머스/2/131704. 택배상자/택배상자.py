def solution(order):
    answer = 0
    
    stack = []
    for idx in range(len(order)):
        stack.append(idx+1)
        
        while stack and stack[-1]==order[answer]:
            stack.pop()
            answer += 1
    return answer
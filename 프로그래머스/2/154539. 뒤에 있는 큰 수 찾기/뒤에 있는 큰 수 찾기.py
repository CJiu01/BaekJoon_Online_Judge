def solution(numbers):
    n = len(numbers)
    answer = [-1]*n
    s = []
    
    for i in range(n):
        while s:
            if numbers[s[-1]]<numbers[i]:
                answer[s[-1]] = numbers[i]
                s.pop()
            else:
                break
        s.append(i)
        
    return answer
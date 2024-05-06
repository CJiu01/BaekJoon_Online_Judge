def solution(numbers):
    answer = ''
    numbers.sort(reverse=True)
    
    for i in numbers:
        answer += str(i)

    return answer
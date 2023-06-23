def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer += (str(i)*(food[i]//2))
    
    tmp = answer[::-1]
    answer += '0'
    answer += str(tmp)

    return answer
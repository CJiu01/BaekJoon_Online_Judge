def solution(array, commands):
    answer = []
    
    for i in commands:
        target = array[i[0]-1:i[1]]
        target.sort()
        answer.append(target[i[2]-1])
    
    return answer
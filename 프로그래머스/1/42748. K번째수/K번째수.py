def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        target = array[commands[i][0]-1:commands[i][1]]
        target.sort()
        answer.append(target[commands[i][2]-1])
    
    return answer
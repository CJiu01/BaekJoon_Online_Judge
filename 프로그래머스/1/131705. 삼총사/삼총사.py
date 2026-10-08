def dfs(arr, number, v):
    global answer 
    
    if len(arr)==3:
        if sum(arr)==0:
            answer += 1
        return
    
    for i in range(v, len(number)):
        arr.append(number[i])
        dfs(arr, number, i+1)
        arr.pop()
    return

def solution(number):
    global answer 
    answer = 0
    dfs([], number, 0)
    
    return answer
def solution(numbers, target):
    answer = 0
    
    def dfs(numbers, idx, res):
        nonlocal answer
    
        if idx==len(numbers):
            if res==target:
                answer+=1
            return
        
        dfs(numbers, idx+1, res+numbers[idx])
        dfs(numbers, idx+1, res-numbers[idx])
    
    dfs(numbers, 0, 0)
    return answer
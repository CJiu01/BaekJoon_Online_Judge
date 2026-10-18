def solution(order):
    answer = 0
    arr = [i for i in range(len(order),0,-1)]
    s = []
    
    for target in order:
        if s and s[-1]==target:
            s.pop()
            answer+=1
            continue
        
        tmp = -1
        while arr:
            top = arr.pop()
            if top==target:
                tmp=top
                answer += 1
                break
            s.append(top)
        if tmp==-1:
            break
        
    return answer
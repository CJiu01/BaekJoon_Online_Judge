def solution(message, spoiler_ranges):
    answer = []
    r = []
    n = len(message)
    masked = [False]*n
    
    for s in spoiler_ranges:
        for i in range(s[0],s[1]+1):
            masked[i] = True 
            
    t= ''
    flag = False
    for i in range(n):
        if message[i]==' ':
            if t=='':
                continue
            if flag and not t in answer:
                answer.append(t)
            elif not flag:
                r.append(t)
            t =''
            flag = False
            continue
        
        if masked[i]:
            flag = True
        t += message[i]
        
    if t!='':
        if flag and not t in answer:
            answer.append(t)
        elif not flag:
            r.append(t)

    return (len(set(answer)-set(r)))
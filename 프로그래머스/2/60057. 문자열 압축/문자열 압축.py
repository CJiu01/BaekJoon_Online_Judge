def solution(s):
    n = len(s)
    answer = n

    for u in range(1, n//2+1):
        sp = []
        for i in range(0, n, u):
            sp.append(s[i:i+u])

        cnt = 1
        res = ''
        prev = sp[0]
        for i in range(1,len(sp)):
            cur = sp[i]
            
            if prev == cur:
                cnt += 1
            elif cnt > 1:
                res += str(cnt)+prev
                cnt = 1
            else:
                res += prev
                
            prev = cur
        if cnt > 1:
            res += str(cnt)+cur
        else:
            res += cur
        
        answer = min(answer, len(res))
    
    return answer
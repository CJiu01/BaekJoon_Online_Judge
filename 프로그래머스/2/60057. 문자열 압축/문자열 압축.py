def solution(s):
    n = len(s)
    answer = n
    

    for u in range(1, n//2+1):
        words = []
        for i in range(0, n, u):
            words.append(s[i:i+u])

        cnt = 1
        res = ''
        for a,b in zip(words, words[1:]+['']):
            if a == b:
                cnt += 1
            elif cnt > 1:
                res += str(cnt)+a
                cnt = 1
            else:
                res += a

        answer = min(answer, len(res))
    
    return answer
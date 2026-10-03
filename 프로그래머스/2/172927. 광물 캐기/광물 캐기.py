def solution(picks, minerals):
    answer = 0
    strong = []
    
    minerals_strong = {"diamond":[25,1], "iron":[5,2], "stone":[1,3]}
    maximum = sum(picks)*5
    i=0
    while i<len(minerals) and i<=maximum:
        tmp = [0,0,0,0]
        cnt = 1
        while cnt%6 != 0 and i<len(minerals) and i<=maximum:
            tmp[0] += minerals_strong[minerals[i]][0]
            tmp[minerals_strong[minerals[i]][1]] += 1
            i += 1
            cnt += 1
        strong.append(tmp)
        
    strong.sort(reverse=True)
    p,q = 0,0
    while p<len(picks) and q<len(strong):
        if picks[p] == 0:
            p+=1
            continue
        if p==0:
            answer += strong[q][1] + strong[q][2] + strong[q][3]
        elif p==1:
            answer += strong[q][1]*5 + strong[q][2] + strong[q][3]
        elif p==2:
            answer += strong[q][1]*25 + strong[q][2]*5 + strong[q][3]
        picks[p]-=1
        q+=1
    
    return answer
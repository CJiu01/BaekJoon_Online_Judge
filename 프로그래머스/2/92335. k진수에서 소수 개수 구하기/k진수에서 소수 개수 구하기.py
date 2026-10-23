def trans(n, k):
    res = []
    while n>0:
        res.append(n%k)
        n//=k
    res.reverse()
    return res

def solution(n, k):
    answer = 0
    r = trans(n,k)
    t = []
    tmp = ''
    for a in r:
        if a==0 and tmp!='':
            t.append(int(tmp))
            tmp = ''
        elif a!=0:
            tmp+=str(a)
        else:
            tmp = ''
    if tmp!= '':
        t.append(int(tmp))

    for i in t:
        if i==1:
            continue
        f = True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                f = False
                break
        if f:
            answer += 1
    
    return answer
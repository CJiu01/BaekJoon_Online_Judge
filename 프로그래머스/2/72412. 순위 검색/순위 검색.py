from bisect import bisect_left

def back(dep, li, res):
    global db
    if dep==4:
        db.append(res+[li[-1]])
        return
    
    for i in range(2):
        res[dep] = li[dep][i]
        back(dep+1, li, res)

    return

def solution(info, query):
    global db
    answer = []
    db = []
    
    for i in info:
        a,b,c,d,e = i.split()
        wc = '-'
        li = [(a,wc),(b,wc),(c,wc),(d,wc),int(e)]
        back(0, li, [0]*4)
        
    dic = {}
    for d in db:
        k = ' '.join(d[:4])
        dic.setdefault(k, []).append(d[4])
        
    for scores in dic.values():
        scores.sort()
        
    for q in query:
        a = q.split()
        k = ' '.join(word for word in a[:-1] if word != 'and')
        target = int(a[-1])
        
        v = dic.get(k, -1)
        if v==-1:
            answer.append(0)
            continue
        res = len(v) - bisect_left(v, target)
        answer.append(res)

    return answer
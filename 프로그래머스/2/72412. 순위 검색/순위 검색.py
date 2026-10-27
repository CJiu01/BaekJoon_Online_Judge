def solution(info, query):
    answer = []
    
    db = {}
    for row in info:
        a,b,c,d,e = row.split()
        for i in [a,'-']:
            for j in [b,'-']:
                for k in [c,'-']:
                    for l in [d,'-']:
                        key = ' '.join([i,j,k,l])
                        db.setdefault(key, []).append(int(e))
                        
    for row in db.values():
        row.sort()
        
    for q in query:
        row = q.split()
        key = ' '.join(word for word in row[:-1] if word!= 'and')
        v = int(row[-1])
        pool = db.get(key, -1)
        if pool == -1:
            answer.append(0)
            continue
        
        l, r, mid = 0, len(pool), 0
        while l<r:
            mid = (l+r)//2
            if pool[mid]<v:
                l = mid+1
            else:
                r = mid
        answer.append(len(pool)-l)

    return answer
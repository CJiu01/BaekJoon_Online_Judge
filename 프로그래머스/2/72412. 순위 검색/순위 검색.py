def solution(info, query):
    answer = []
    
    db = {}
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    db.setdefault((a,b,c,d),[])
    
    for row in info:
        a,b,c,d,e = row.split()
        for i in [a,'-']:
            for j in [b,'-']:
                for k in [c,'-']:
                    for l in [d,'-']:
                        db[(i, j, k, l)].append(int(e))
                        
    for row in db.values():
        row.sort()
        
    for q in query:
        row = q.split()
        pool = db[(row[0],row[2],row[4],row[6])]
        v = int(row[-1])
        
        l, r, mid = 0, len(pool), 0
        while l<r:
            mid = (l+r)//2
            if pool[mid]<v:
                l = mid+1
            else:
                r = mid
        answer.append(len(pool)-l)

    return answer
def back(degree, n, cur, v):
    global pool
    if len(cur) == n:
        pool.append(cur[:])
        return
    
    for i in range(v, degree):
        cur.append(i)
        back(degree, n, cur, i+1)
        cur.pop()
    return

def solution(relation):
    global pool
    answer = []
    pool = []
    degree = len(relation[0])
    cardinarity = len(relation)
    
    for i in range(1, degree+1):
        back(degree, i, [], 0)
        
    for p in pool:
        f = True
        for a in answer:
            x, y = set(a), set(p)
            if x & y == x:
                f = False
                break
        if not f:
            continue
        
        t = set()
        for r in relation:
            k = ' '.join([r[i] for i in p])
            t.add(k)
        if len(t) == cardinarity:
            answer.append(p)
            
    return len(answer)
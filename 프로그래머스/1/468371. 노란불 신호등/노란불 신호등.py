import math

def solution(signals):
    answer = 0
    
    # lcm
    n = 1
    for s in signals:
        n = math.lcm(n,sum(s))
        
    a = [[0] for _ in range(len(signals))]
    for i in range(len(signals)):
        t = signals[i][1]
        idx = signals[i][0]+1
        d = signals[i][0] + signals[i][2]
        
        while idx<=n:
            a[i].extend([j for j in range(idx, idx+t)])
            idx += t+d

    res = set(a[0][1:])
    for i in range(1,len(a)):
        res = res & set(a[i][1:])

    return min(res) if res else -1  
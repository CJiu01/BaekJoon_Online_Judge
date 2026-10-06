def solution(k, ranges):
    seq = [k]
    answer = []

    while k>1:
        if k%2==0:
            k//=2
        else:
            k = k*3+1
        seq.append(k)
    
    n = len(seq)-1
    sizes = [0]
    size = 0
    for i in range(n):
        size += (seq[i]+seq[i+1])/2
        sizes.append(size)
    
    for r in ranges:
        if n+r[1] < r[0]:
            answer.append(-1.0)
        else:
            s = sizes[n+r[1]]-sizes[r[0]]
            answer.append(s)
        
    return answer

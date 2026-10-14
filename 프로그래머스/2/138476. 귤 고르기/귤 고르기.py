from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    n = len(counter)
    counter = counter.most_common()

    cnt = 0
    kind = []
    for i in range(n):
        cnt += counter[i][1]
        kind.append(counter[i][0])
        
        if cnt>=k:
            return len(kind)   
    return n
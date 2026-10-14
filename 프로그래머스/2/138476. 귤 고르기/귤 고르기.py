from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine).most_common()
    
    for a,v in counter:
        k -= v
        answer += 1
        if k<=0:
            break
    return answer
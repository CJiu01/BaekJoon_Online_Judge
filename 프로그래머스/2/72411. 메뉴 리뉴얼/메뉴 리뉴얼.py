from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    n = len(orders)
    set_name = [[] for _ in range(course[-1]+1)]
    
    for i in range(n):
        order_a = set(orders[i])
        for j in range(i+1, n):
            order_b = set(orders[j])
            same_al = ''.join(sorted(order_a.intersection(order_b)))

            for k in course:
                if k>len(same_al):
                    break
                tmp = list(combinations(same_al, k))
                for t in tmp:
                    set_name[k].append(''.join(t))

    for s in set_name:
        if not s:
            continue
        c = Counter(s)
        max_value = c.most_common(1)[0][1]

        for k,v in c.items():
            if v<max_value:
                continue
            answer.append(k)

    return sorted(answer)

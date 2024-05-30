from collections import Counter

def solution(clothes):
    answer = 1
    
    clothes_kind = []
    for item in clothes:
        clothes_kind.append(item[1])
    clothes_kind = Counter(clothes_kind)
    
    for item in clothes_kind:
        answer *= (clothes_kind[item]+1)

    return (answer-1)
# from collections import Counter

# def solution(clothes):
#     answer = 1
    
#     clothes_kind = []
#     for item in clothes:
#         clothes_kind.append(item[1])
#     clothes_kind = Counter(clothes_kind)
    
#     for item in clothes_kind:
#         answer *= (clothes_kind[item]+1)

#     return (answer-1)


def solution(clothes):
    clothes_type = {}
    
    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1
            
    cnt = 1
    for num in clothes_type.values():
        cnt *= num
        
    return cnt - 1
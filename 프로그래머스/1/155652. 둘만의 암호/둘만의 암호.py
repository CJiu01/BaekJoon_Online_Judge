def solution(s, skip, index):
    answer = ''
    spec = make_spec(skip)
    for al in s:    
        answer += spec[(spec.index(al)+index)%(len(spec))]

    return answer

def make_spec(skip):
    special = ''
    alph = [chr(i+97) for i in range(26)]
    
    for i in alph:
        if i in skip:
            continue
        special+=i
    return special
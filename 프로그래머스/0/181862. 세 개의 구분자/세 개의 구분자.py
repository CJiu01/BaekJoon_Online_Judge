def solution(myStr):
    answer = []
    str = ''
    for s in myStr:
        if s in ['a','b','c']:
            if str != '':
                answer.append(str)
                str=''
            continue
        str+=s
        
    
    if str != '':
        answer.append(str)
    elif not answer:
        answer.append("EMPTY")
    
    return answer
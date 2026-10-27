def solution(s):
    answer = []
    
    a = s.replace('{{','').replace('}}','').split('},{')
    b = []
    for i in a:
        b.append(list(map(int, i.split(','))))
        
    b.sort(key= lambda x:len(x))
    
    for t in b:
        v = list(set(t) - set(answer))
        answer.extend(v)
    
    return answer
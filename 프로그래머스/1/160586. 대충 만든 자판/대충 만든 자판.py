def count(target, al):
    cnt = 0
    for i in range(len(target)):
        a = ord(target[i])-65
        if al[a]<=100:
            cnt+=al[a]
        else:
            return -1
    return cnt
    
def solution(keymap, targets):
    answer = []

    for key in keymap:
        for i in range(len(key)):
            a = ord(key[i])-65
            al[a] = min(al[a], (i+1))
            
    for target in targets:
        answer.append(count(target, al))
    
    return answer

al = [101]*26
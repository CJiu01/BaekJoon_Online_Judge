def trans(n):
    a = ''
    while n>0:
        a += str(n%2)
        n //= 2
    return a[::-1]

def solution(s):
    i, cnt = 0,0
    
    while s!='1':
        zero = s.count('0')
        cnt += zero
        s = len(s)-zero
        s = trans(s)
        i+=1
    
    return [i, cnt]
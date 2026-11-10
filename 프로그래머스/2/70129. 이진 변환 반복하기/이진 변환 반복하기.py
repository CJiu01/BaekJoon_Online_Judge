
def solution(s):
    a,b = 0,0
    
    while s != '1':
        num = s.count('1')
        b += len(s)-num
        s = bin(num)[2:]
        a+=1

    return [a,b]
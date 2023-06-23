def solution(t, p):
    length = len(p)
    p = int(p)
    result = 0
    for i in range(len(t)-length+1):
        number = ''
        for j in range(i,i+length):
            number += t[j]
        if int(number) <= p:
            result += 1
    return result
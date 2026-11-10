def solution(w,h):
    cnt = 0 
    a = -h/w
    for x in range(1,w):
        y = a*x + h
        if y<1: 
            break
        cnt += int(y)

    return cnt*2
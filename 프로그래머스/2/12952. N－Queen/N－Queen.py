def solution(n):
    queen(0,n)
    return cnt

def queen(k,n):
    global cnt
    
    if k==n:
        cnt+=1
        return
    
    for i in range(n):
        if (isused1[i]==False and isused2[k+i]==False and isused3[k-i+n-1]==False):
            isused1[i] = True
            isused2[k+i] = True
            isused3[k-i+n-1] = True

            queen(k+1,n)
            isused1[i] = False
            isused2[k+i] = False
            isused3[k-i+n-1] = False

    return

cnt = 0
isused1 = [False]*50
isused2 = [False]*50
isused3 = [False]*50


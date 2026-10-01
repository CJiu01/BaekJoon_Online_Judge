def solution(storey):
    answer = 0
    storey = str(storey)
    n = len(storey)
    
    i = 1
    while int(storey)>0:
        num = int(storey[-1*i])
        if num == 5:
            k=1
            while i<n and n-i-k>=0 and int(storey[(-1*i)-k])+1 == 5:
                k+=1
                
            if i==n or n-i-k<0 or int(storey[(-1*i)-k])+1<5:
                tmp = num
                answer += tmp
                storey = int(storey) - (tmp * 10**(i-1))
            else:
                tmp = (10-num)
                answer += tmp
                storey= int(storey) + (tmp * 10**(i-1))
                
        elif  num> 5: 
            tmp = (10-num)
            answer += tmp
            storey= int(storey) + (tmp * 10**(i-1))
        else:
            tmp = num
            answer += tmp
            storey = int(storey) - (tmp * 10**(i-1))
            
        storey = str(storey)
        i+=1

    return answer
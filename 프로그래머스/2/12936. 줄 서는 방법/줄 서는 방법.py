from math import factorial

def solution(n, k):
    
    arr = [i for i in range(1,n+1)]
    answer = []
    
    while arr:
        a = (k-1) // factorial(n-1)
        answer.append(arr.pop(a))
        
        k = k%factorial(n-1)
        n -= 1
        
    return answer
from itertools import permutations

def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    
    whole = []
    for i in range(1,len(numbers)+1):
        whole += permutations(numbers, i)
    
    b= []
    for i in whole:
        b.append(int(''.join(i)))
    b = set(b)
    
    for i in b:
        if i > 1:
            if is_prime(i):
                answer += 1
                
    return answer
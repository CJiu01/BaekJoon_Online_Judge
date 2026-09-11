            
def solution(number, limit, power):
    divisors = [0] * (number+1)
    for i in range(1, number+1):
        for j in range(i, number+1, i):
            divisors[j] += 1
    
    answer  = 0
    for d in divisors:
        if d<=limit:
            answer += d
        else:
            answer += power
    return answer
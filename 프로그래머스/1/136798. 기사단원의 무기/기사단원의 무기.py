def count(n):
    cnt = 2
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            if (n**0.5) != i:
                cnt += 2
            else:
                cnt += 1
    return cnt

def solution(number, limit, power):
    answer = [1]
    for i in range(2,number+1):
        answer.append(count(i))
    needed = 0
    for num in answer:
        if num<=limit:
            needed += num
        else:
            needed += power
    
    return needed
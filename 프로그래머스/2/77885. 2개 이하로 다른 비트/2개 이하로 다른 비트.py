def solution(numbers):
    answer = []
    
    for n in numbers:
        if n%2 == 0:
            answer.append(n+1)
            continue
        b = [0]
        b += list(map(int, bin(n)[2:]))
        
        for i in range(1, len(b)+1):
            if b[-i] == 0:
                b[-i] = 1
                b[-i+1] = 0
                answer.append(int(''.join(map(str, b)),2))
                break

    return answer
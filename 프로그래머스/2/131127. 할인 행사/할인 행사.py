from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    d = []
    for (a,b) in zip(want, number):
        d.extend([a]*b)
    d = Counter(d)
   
    for i in range(len(discount)-9):
        window = discount[i:i+10]
        c = Counter(window)
        tmp = d-c
        if len(d-c)==0:
            answer+=1
            
    return answer

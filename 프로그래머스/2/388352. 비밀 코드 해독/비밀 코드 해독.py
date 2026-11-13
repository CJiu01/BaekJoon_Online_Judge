from itertools import combinations

def solution(n, q, ans):
    answer = 0
    l = [i for i in range(1,n+1)]
    
    for c in combinations(l, 5):
        tmp = []
        
        for check in q:
            cnt = 0
            for i in c:
                if i in check:
                    cnt += 1
            tmp.append(cnt)
        
        if tmp==ans:
            answer+=1
    
    return answer
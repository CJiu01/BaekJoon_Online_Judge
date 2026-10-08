
def win_arr(info):
    ryan = [0]*11
    for i in range(10):
        ryan[i] = info[i]+1
        
    return ryan

def back(dep, ryan, v, n, win_for_ryan):
    global res
    if dep == 0 :
        if sum(ryan)<=n:
            tmp = ryan.copy()
            tmp[10] += n-sum(ryan)
            res.append(tmp.copy())
        return
    
    for i in range(v,11):
        if sum(ryan) + win_for_ryan[i] <= n:
            ryan[i] += win_for_ryan[i]
            back(dep-1, ryan, i+1, n, win_for_ryan)
            ryan[i] -= win_for_ryan[i]
        
def score(info):
    global res
    best, best_diff = [-1],0
    
    for r in res:
        apeach, ryan = 0,0  
        for i in range(11):
            if info[i] == 0 and r[i] == 0:
                continue
            if info[i] >= r[i]:
                apeach += 10-i
            else:
                ryan += 10-i
        
        if ryan>apeach:
            d = ryan-apeach
            if d>best_diff or d==best_diff and r[::-1]>best[::-1]:
                best,best_diff = r,d
    return best
    

def solution(n, info):
    global res
    res = []
    
    win_for_ryan = win_arr(info)
    
    for i in range(11):
        back(i, [0]*11, 0, n, win_for_ryan)
    answer = score(info)
    
    return answer
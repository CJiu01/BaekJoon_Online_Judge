
def solution(diffs, times, limit):
    answer = 0
    start = 1
    end = max(diffs)
    
    while start<=end:
        lv = (start+end) // 2
        user = 0
        for i in range(len(diffs)):
            if lv-diffs[i]<0:
                prev = times[i-1] if i>0 else 0
                user += (diffs[i]-lv)*(prev+times[i])
            user += times[i]
        if user<= limit:
            answer = lv
            end = lv-1
        else:
            start = lv+1
    
    return answer
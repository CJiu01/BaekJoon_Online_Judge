
def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    startday -= 1
    
    for i in range(n):
        
        d = schedules[i] + 10
        if d % 100 >= 60:
            d = ((d//100)+1)*100 + (d%100)%60
        f = True
        s = startday
        for time in timelogs[i]:
            if s%7>4:
                s += 1
                continue
            if time>d:
                f = False
                break
            s += 1
        if f:
            answer+=1

    return answer
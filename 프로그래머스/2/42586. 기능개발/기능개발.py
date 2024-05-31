import math

def solution(progresses, speeds):
    answer = []
    released = [False]*len(progresses)
    left = cal_completed_days(progresses, speeds)

    i = 0
    while i < (len(progresses)):
        cnt = 0
        if released[i] == False:
    
            day = left[i]
            released[i] = True
            cnt += 1
            
            while i<len(progresses)-1:
                if left[i+1] > day:
                    break
                else:
                    released[i+1] = True
                    cnt += 1
                    i += 1
        i+=1
        print("cnt: ",cnt)
        answer.append(cnt)

    return answer

def cal_completed_days(progresses,speeds):
    left = []
    
    for i in range(len(progresses)):
        day = 100-progresses[i]
        left.append(math.ceil(day/speeds[i]))
    return left
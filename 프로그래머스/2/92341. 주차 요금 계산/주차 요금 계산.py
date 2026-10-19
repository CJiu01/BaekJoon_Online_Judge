import math 
def change_to_minutes(t):
    h,m = map(int, t.split(':'))
    t = h*60+m
    return t

def solution(fees, records):
    answer = {}
    
    new_records = []
    for r in records:
        t, n, type = r.split()
        new_records.append([int(n), change_to_minutes(t), type])
    new_records.sort()    
    
    n = len(new_records)
    i = 0
    while i < n:
        last, num = 0, new_records[i][0]
        while i<n and new_records[i][0] == num:
            if i+1<n and new_records[i][0]==new_records[i+1][0]:
                last += (new_records[i+1][1] - new_records[i][1])
                i+=2
            else:
                last += (1439 - new_records[i][1])
                i+=1
                
        fee = fees[1]
        last -= fees[0]
        if last>0:
            fee += math.ceil(last/fees[2])*fees[3]
        answer[num] = answer.get(num,0)+ fee
        
    return list(answer.values())
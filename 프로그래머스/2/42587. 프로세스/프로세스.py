def solution(priorities, location):
    data = []
    for i in range(len(priorities)):
        data.append([priorities[i], i])
    
    target = 0 
    order = 0

    while True:
        if data[target][0] == max(data, key= lambda x: x[0])[0]:
            order += 1
            if data[target][1] == location:
                return order
            data.pop(target)
        else:
            target += 1
        
        if target == len(data):
            target = 0
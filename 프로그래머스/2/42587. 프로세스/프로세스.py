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
    
# v2    
def solution(priorities, location):
    answer = 0
    search, c = sorted(priorities, reverse=True), 0
    while True:
        for i, priority in enumerate(priorities):
            s = search[c]
            if s == priority:
                c += 1
                answer += 1
                if i == location:
                    break
        else:
            continue
        break
    return answer


# v3
def solution(priorities, location):
    answer = 0
    queue = [(i,p) for i,p in enumerate(priorities)]
    
    while True:
        print(queue)
        cur = queue.pop(0)
        if any(cur[1]<q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

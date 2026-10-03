def solution(plans):
    answer = []
    n = len(plans)
    for i in range(n):
        time = list(map(int, plans[i][1].split(":")))
        plans[i] = [plans[i][0], time[0]*60 + time[1], int(plans[i][2])]
    
    plans.sort(key = lambda x: x[1])
    
    stops = []
    for i in range(n-1):
        posible_time = plans[i+1][1] - plans[i][1]
        
        if posible_time >= plans[i][2]:  
            answer.append(plans[i][0])
            posible_time -= plans[i][2]
            
            while posible_time>0 and stops:
                stop_last = stops.pop()
                if stop_last[1] <= posible_time:
                    answer.append(stop_last[0])
                    posible_time -= stop_last[1]
                else:
                    stops.append([stop_last[0],stop_last[1]-posible_time])
                    break
        else:
            stops.append([plans[i][0], plans[i][2]-posible_time])

    answer.append(plans[-1][0])
    stops.reverse()
    for stop in stops:
        answer.append(stop[0])

    return answer
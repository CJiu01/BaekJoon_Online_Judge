import heapq as hq

def solution(jobs):
    answer = 0
    n = len(jobs)
    jobs.sort()
    
    i, time = 0,0
    h = []
    while i<n or h:
        # 해당시간까지 온 작업 heap에 넣기
        while i<n:
            if jobs[i][0]>time:
                break
            hq.heappush(h, [jobs[i][1], jobs[i][0], i])
            i += 1
        
        # 해당시간까지 온 job이 없는 경우
        if not h:
            time = jobs[i][0]
            continue
            
        cur_job = hq.heappop(h)
        time += cur_job[0]
        answer += (time-cur_job[1])  
    answer //= n
    
    return answer
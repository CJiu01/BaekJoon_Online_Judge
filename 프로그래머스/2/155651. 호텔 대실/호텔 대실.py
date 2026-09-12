def solution(book_time):
    time_table = [0 for _ in range(60*24)]
    for start, end in book_time:
        start_minutes = int(start[:2])*60 + int(start[3:])
        end_minutes = int(end[:2])*60 + int(end[3:])+10
        
        if end_minutes> 60*24-1:
            end_minutes = 60*24-1
        
        for i in range(start_minutes, end_minutes):
            time_table[i] += 1
            
    return max(time_table)
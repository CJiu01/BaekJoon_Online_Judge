def to_seconds(times):
    res = []
    for t in range(len(times)):
        m,s = map(int, times[t].split(':'))
        if t==1: s+=10
        res.append(m*60+s)
    return res

def solution(book_time):
    answer = 0
    
    for i in range(len(book_time)):
        book_time[i] = to_seconds(book_time[i])
        
    book_time.sort()
    room = []
    room.append(book_time[0][1])
    
    for i in range(1,len(book_time)):
        idx = 1000
        room.sort()
        for j in range(len(room)):
            if book_time[i][0] >= room[j]:
                idx = j
                break
        if idx == 1000:
            room.append(book_time[i][1])
        else: 
            room[idx] = book_time[i][1]
        
    return len(room)
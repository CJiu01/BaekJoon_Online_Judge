def to_seconds(time):
    m, s = map(int, time.split(':'))
    return m*60 + s
   
def solution(video_len, pos, op_start, op_end, commands):
    video_len = to_seconds(video_len)
    pos = to_seconds(pos)
    op_start = to_seconds(op_start)
    op_end = to_seconds(op_end)
    
    for c in commands:
        if op_start<=pos<op_end:
            pos = op_end
        
        if c == 'prev':
            pos -= 10
        else:
            pos += 10
            
        if pos<0:
            pos = 0
        elif pos>video_len:
            pos = video_len
        
    if op_start<=pos<op_end:
        pos = op_end

    answer = f'{pos//60:02d}:{pos%60:02d}'
    return answer
def solution(data, col, row_begin, row_end):
    answer = 0
    
    data.sort(key=lambda x:(x[col-1],-x[0]))
    
    for row in range(row_begin-1, row_end):
        mod = sum(i%(row+1) for i in data[row])
        answer ^= mod
    
    return answer
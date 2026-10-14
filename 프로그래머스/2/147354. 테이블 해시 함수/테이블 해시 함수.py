def solution(data, col, row_begin, row_end):
    answer = -1
    data.sort(key=lambda x:(x[col-1],-x[0]))

    for row in range(row_begin-1, row_end):
        mod = 0
        for i in data[row]:
            mod += (i%(row+1))
        
        if answer==-1:
            answer=mod
        else:
            answer ^= mod
    return answer
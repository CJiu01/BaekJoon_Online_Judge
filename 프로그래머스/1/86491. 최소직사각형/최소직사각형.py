def solution(sizes):   
    for i in sizes:
        i.sort()
    row = max(sizes, key= lambda x: x[0])[0]
    col = max(sizes, key= lambda x: x[1])[1]

    return row*col
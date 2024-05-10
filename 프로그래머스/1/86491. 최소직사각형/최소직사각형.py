def solution(sizes):
    answer = 0
    
    for i in sizes:
        i.sort()
        
    max_width = 0
    max_length = 0
    
    for i in sizes:
        if max_width < i[0]:
            max_width = i[0]
        if max_length < i[1]:
            max_length = i[1]
        
    return max_length * max_width
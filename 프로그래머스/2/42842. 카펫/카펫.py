def solution(brown, yellow):    
    row,col = 1,1
    for col in range(1,yellow):
        if yellow%col != 0:
            continue
        row = yellow//col
        if ((row+2)+col)*2 == brown:
            break
            
    return [row+2, col+2]
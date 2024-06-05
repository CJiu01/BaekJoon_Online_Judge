def solution(brown, yellow):
    answer = []
    
    row,col = 1,1
    for col in range(1,yellow):
        if yellow%col != 0:
            print("continue")
            continue
        
        row = yellow//col
        
        if ((row+2)+col)*2 == brown:
            break
        
    answer.append(row+2)
    answer.append(col+2)
    return answer
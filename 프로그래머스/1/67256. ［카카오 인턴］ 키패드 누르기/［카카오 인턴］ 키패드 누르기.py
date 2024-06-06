def moved_distance(current, target):
    d = abs(current-target)  
    if d%3 == 0:
        return d//3
    else:
        return (d//3 + d%3)

def solution(numbers, hand):
    answer = []
    left_side = [1,4,7]
    right_side = [3,6,9]
    left_position = 10
    right_position = 12
    
    for target in numbers:
        
        if target == 0:
            target = 11
        
        if target in left_side:
            dir = 'L'
        elif target in right_side:
            dir = 'R'
        else:
            tmp_left = moved_distance(left_position, target)
            tmp_right = moved_distance(right_position, target)
            if tmp_left > tmp_right:
                dir = 'R'
            elif tmp_left < tmp_right:
                dir = 'L'
            else:
                if hand == 'right':
                    dir = 'R'
                else:
                    dir = 'L'
        
        if dir == 'L':
            answer.append('L')
            left_position = target
        else:
            answer.append('R')
            right_position = target
            
    return ''.join(answer)
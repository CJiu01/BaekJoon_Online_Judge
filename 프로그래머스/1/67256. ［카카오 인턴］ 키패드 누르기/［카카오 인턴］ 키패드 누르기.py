# def moved_distance(current, target):
#     d = abs(current-target)  
#     if d%3 == 0:
#         return d//3
#     else:
#         return (d//3 + d%3)

# def solution(numbers, hand):
#     answer = []
#     left_side = [1,4,7]
#     right_side = [3,6,9]
#     left_position = 10
#     right_position = 12
    
#     for target in numbers:
        
#         if target == 0:
#             target = 11
        
#         if target in left_side:
#             dir = 'L'
#         elif target in right_side:
#             dir = 'R'
#         else:
#             tmp_left = moved_distance(left_position, target)
#             tmp_right = moved_distance(right_position, target)
#             if tmp_left > tmp_right:
#                 dir = 'R'
#             elif tmp_left < tmp_right:
#                 dir = 'L'
#             else:
#                 if hand == 'right':
#                     dir = 'R'
#                 else:
#                     dir = 'L'
        
#         if dir == 'L':
#             answer.append('L')
#             left_position = target
#         else:
#             answer.append('R')
#             right_position = target
            
#     return ''.join(answer)

def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}
    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])
            
            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i
    return answer
import math

def solution(signals):
    
    lcm = 1
    for s in signals:
        a = sum(s)
        lcm = math.lcm(lcm,a)
    
    for t in range(1, lcm+1):
        is_all_yellow = True
        
        for g, y, r in signals:
            cycle_length = g+y+r
            
            current_pos = t % cycle_length
            if not (g+1<= current_pos <= g+y):
                is_all_yellow = False
                break
            
        if is_all_yellow:
            return t
        
    return -1
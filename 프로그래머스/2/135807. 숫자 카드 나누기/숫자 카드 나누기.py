import math 

def solution(arrayA, arrayB):
    gcd_A, gcd_B = math.gcd(*arrayA), math.gcd(*arrayB)
    
    for a in arrayA:
        if a%gcd_B==0:
            gcd_B = 0
            break
    for b in arrayB:
        if b%gcd_A==0:
            gcd_A = 0
            break 

    return max(gcd_A, gcd_B)
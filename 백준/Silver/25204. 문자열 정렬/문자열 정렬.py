import sys
input = sys.stdin.readline
from functools import cmp_to_key

def compare(x, y):
    len_x = len(x)
    len_y = len(y)
    i = 0
    while (i<len_x and i<len_y):
        if (x[i] != y[i]):
            if (x[i] != '-' and y[i] == '-'):
                return -1
            elif (x[i] == '-' and y[i] != '-'):
                return 1
            
            x_low = x[i].lower()
            y_low = y[i].lower()
            
            if (x_low != y_low):
                return 1 if (x_low>y_low) else -1
            
            if (x[i] != y[i]):
                return 1 if (x[i]>y[i]) else -1
            
        i+=1
    if (len_x>len_y):
        return 1
    elif (len_x<len_y):
        return -1
    else:
         return 0
            

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [input().rstrip() for _ in range(n)]
    
    arr.sort(key=cmp_to_key(compare))
    print('\n'.join(arr))
import sys
input = sys.stdin.readline

def solution():
    result = [0]*n
    
    for i in range(n):
        cnt = 0
        idx = 0

        while cnt < queue[i]:
            if result[idx] == 0:
                cnt += 1
            idx += 1
        
        for k in range(idx, n):
            if result[k] == 0: 
                result[k] = i+1
                break
            
    return result

n = int(input())
queue = list(map(int, input().split()))

print(*solution())
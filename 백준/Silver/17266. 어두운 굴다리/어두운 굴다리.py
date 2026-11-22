import math
def solution(n,m,pos):
    length = max(pos[0], n-pos[-1])
    for i in range(1,m):
        length = max(length, math.ceil((pos[i]-pos[i-1])/2))
    return length

n = int(input())
m = int(input())
pos = list(map(int, input().split()))
print(solution(n,m,pos))
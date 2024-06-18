from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
wheel = []
for i in range(T):
    wheel.append(deque(map(int, input().strip())))

K = int(input())
dir = []
for i in range(K):
    dir.append(list(map(int,input().split())))



for i in range(K):
    
    move = [0]*T
    target = dir[i][0]-1
    move[target] = dir[i][1]
    
    # 증가
    right = target+1
    left = target
    while right<T:
        if wheel[left][2] == wheel[right][6]:
            move[right] = 0
            break
        else:
            move[right] = -move[left]
            left = right
            right += 1
    
    # 감소
    right = target
    left = target-1
    while left>=0:
        if wheel[right][6] == wheel[left][2]:
            move[left] = 0
            break
        else:
            move[left] = -move[right]
            right = left
            left -= 1
    
    # move 배열적용
    for i in range(T):
        if move[i] == 1: # 시계
            tmp = wheel[i].pop()
            wheel[i].appendleft(tmp)
        elif move[i] == -1: # 반시계
            tmp = wheel[i].popleft()
            wheel[i].append(tmp)
    
res = 0
for i in wheel:
    if i[0] == 1:
        res += 1
print(res)
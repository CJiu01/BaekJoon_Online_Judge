import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
belt = deque(map(int,input().split()))
robot = deque([0 for _ in range(n)])
res = 0
cnt = 1


while k>0:
    belt.appendleft(belt.pop())
    robot.pop()
    robot.appendleft(0)
    robot[-1] = 0
    for i in range(n-2,0,-1):
        if robot[i] and (robot[i+1]==0 or (i+1)==n) and belt[i+1]>=1:
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1

            if belt[i+1] == 0:
                res += 1
    if belt[0]>0:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            res += 1
    if res>=k:
        print(cnt)
        break
    cnt += 1


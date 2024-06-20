import sys
input = sys.stdin.readline

n = int(input())
cars = {}
for i in range(n):
    num = input().strip()
    cars[num] = i+1

cnt = 0
stack = []
for i in range(n):
    out_num = input().strip()
    while stack and stack[-1] > cars[out_num]:
        stack.pop()
        cnt += 1
    stack.append(cars[out_num])
print(cnt)
import sys
input = sys.stdin.readline

num = input().strip()
length = len(num)
half = length//2

front, rear = 0, 0
for i in range(half):
    front += int(num[i])
    rear += int(num[length-i-1])

if front==rear:
    print('LUCKY')
else:
    print('READY')
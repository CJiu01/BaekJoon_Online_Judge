import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    digit_sum = i + sum(map(int, str(i)))
    if digit_sum == n:
        print(i)
        break
else:
    print(0)
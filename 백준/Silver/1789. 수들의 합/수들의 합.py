import sys
input = sys.stdin.readline

S = int(input())
N = 1
i = 1
while True:
    if S-i>i:
        S -= i
        N += 1
        i += 1
    else:
        break
print(N)
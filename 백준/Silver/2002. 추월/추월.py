import sys
input = sys.stdin.readline

n = int(input())
entrance = {}
for i in range(n):
    num = input().strip()
    entrance[num] = i+1
    
exit = {}
for i in range(n):
    num = input().strip()
    ord = entrance[num]
    exit[num] = ord

exit = list(exit.values())
cnt = 0
f = [False]*n

for i in range(1,n):
    j = i-1
    while j>=0:
        if exit[j] > exit[i] and f[j] == False:
            f[j] = True
            cnt += 1
        j -= 1

print(cnt)
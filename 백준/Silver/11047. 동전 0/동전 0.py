import sys
n, k = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))

array.sort(reverse=True)

count = 0
for i in array:
    if k == 0:
        break
    if k//i >0:
        count += (k//i)
        k %= i 
    

print(count)
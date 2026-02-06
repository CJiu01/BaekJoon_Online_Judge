import sys
input = sys.stdin.readline

number = input().strip()
arr = [0]*9

for i in number:
    n = int(i)
    if n==9:
        arr[6]+=1
    else:
        arr[n]+=1
        
if arr[6]%2 == 0:
    arr[6] //= 2
else:
    arr[6] //= 2
    arr[6] += 1
    
print(max(arr))

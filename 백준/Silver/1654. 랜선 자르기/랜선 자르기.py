import sys

n, k = map(int, input().split())
array =[]
for _ in range(n):
    array.append(int(sys.stdin.readline()))

start = 1
end = max(array)

result = 0
while(start <= end):
    mid = (start+end) // 2
    total = 0
    
    for i in array:
        total += (i//mid)
    if total >= k :
        start = mid+1
        result = mid
    else:
        end = mid-1
        
print(result)
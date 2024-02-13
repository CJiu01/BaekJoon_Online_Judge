import sys
input = sys.stdin.readline

n,c = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

def binary(start, end):
    result = 0
    while start<=end:
        mid = (start+end) // 2
        current = arr[0]
        cnt = 1
        
        for i in range(1,n):
            if arr[i] >= current + mid:
                cnt += 1
                current = arr[i]
                
        if cnt >= c:
            start = mid+1
            result = mid
        else:
            end = mid-1
            
    return result
  
start = 1
end = arr[-1]-arr[0]
print(binary(start,end))
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

def binary(start, end):
    result = 0
    while start<=end:
        mid = (start+end) // 2
        
        total = 0
        for i in arr:
            if i>mid:
                total += (i-mid)
        if total>=m:
            start = mid+1
            result = mid
        else:
            end = mid-1
    return result

print(binary(0,max(arr)))
import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
a = list(map(int, input().split()))
b= list(map(int,input().split()))
a.sort()
b.sort()

A = set()
for i in range(n-1):
    for j in range(i+1,n):
        A.add(a[j]-a[i])

a = list(A)
a.sort()
        
def binary(i):
    start = 0
    end = m-1
    
    triangle = -1
    while start<=end:
        mid = (start+end) // 2
        s = i*b[mid]/2
        if s<=r:
            start = mid+1
            if s>triangle:
                triangle=s
        else:
            end = mid-1

    return triangle
   
result = -1
for i in a:
    current = binary(i)
    if current > result:
        result = current
print(result)
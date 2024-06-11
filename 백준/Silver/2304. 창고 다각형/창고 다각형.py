import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
    
arr.sort()

left,right = 0,0
res = 0
dir = True

while left < n-1:
    for j in range(left+1,n):
        if arr[left][1] <= arr[j][1]:
            right = j
            dir = True
            break
    else:
        right = left+1
        for j in range(left+2,n):
            if arr[j][1] >= arr[right][1]:
                right = j        
        res += arr[left][1] 
        dir = False
        
    if dir:
        res += (arr[right][0]-arr[left][0])*arr[left][1]      
    else:
        res += (arr[right][0]-arr[left][0]-1)*arr[right][1]
        
    left = right       
    
res += arr[right][1]   
print(res)
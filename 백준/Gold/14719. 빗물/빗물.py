import sys
input = sys.stdin.readline

h,w = map(int,input().split())
block = list(map(int, input().split()))

res = 0
left = 0
for i in range(len(block)):
    if block[i]>left:
        left = i
        break
  
while left != (w-1):
    max_block = 0
    right = 0
    
    for i in range(left+1,w):
        if block[i] >= max_block:
            right = i
            max_block = block[i]
            
    if max_block == 0:
        break
         
    if right-left > 1:
        a = min(block[left],block[right])
        left_idx = left

        for j in range(left+1, right):
            
            
            if block[left_idx] < block[j]:
                left_idx = j
            a = min(block[left_idx],block[right])
            
            res += abs(a-block[j])
    
    left = right

print(res)
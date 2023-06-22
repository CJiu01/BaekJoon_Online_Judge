N = int(input())
li = list(map(int, input().split()))
find = int(input())
cnt = 0
for i in li:
    if i == find:
        cnt += 1
        
print(cnt)
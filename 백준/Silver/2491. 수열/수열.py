n = int(input())
arr = list(map(int, input().split()))
len_arr = len(arr)
res = 1
i, inc = 1,1
# 증가
while i<len_arr:
    if (arr[i-1]<=arr[i]):
        inc += 1
        res = max(res, inc)
    else:
        inc = 1
    i+=1

i,dec = 1,1
# 감소
while i<len_arr:
    if (arr[i-1]>=arr[i]):
        dec += 1
        res = max(res, dec)
    else:
        dec = 1
    i+=1
        
print(res)
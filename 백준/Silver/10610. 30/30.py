array = list(map(int, input()))

flag = False
total = 0
for i in array:
    if i==0:
        flag= True
    total += i

if flag and total%3==0:
    array.sort(reverse=True)
    print(*array,sep='')
else:
    print("-1")
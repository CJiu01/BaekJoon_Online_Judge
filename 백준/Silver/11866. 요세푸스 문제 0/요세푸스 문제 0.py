n, k = map(int, input().split(' '))
mans = [i+1 for i in range(n)]

cnt = 1
res = []
while len(mans) > 0:
    N = len(mans)
    tmp = []
    for i in range(N):
        if cnt%k == 0:
            tmp.append(i)
            res.append(mans[i])
        cnt += 1
    for i in range(len(tmp)):
        mans.pop(tmp[i]-i)
print('<',end='')
print(*res,sep=', ',end='')
print('>')
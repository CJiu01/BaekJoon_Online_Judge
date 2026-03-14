N = int(input())

for _ in range(N):
    y_cnt = 0
    k_cnt = 0
    for _ in range(9):
        y,k=map(int,input().split())
        y_cnt += y
        k_cnt += k
    if y_cnt>k_cnt:
        print('Yonsei')
    elif k_cnt>y_cnt:
        print('Korea')
    else:
        print('Draw')
        
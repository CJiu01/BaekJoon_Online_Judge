import sys
input = sys.stdin.readline

def cal(h1, m1, h2, m2):
    a = h1- h2
    b = m1 - m2
    if b<0:
        b += 60
        a -= 1
    return a,b

n = int(input())
info = []
for _ in range(n):
    a,b = input().split()
    h,m = b[0:2], b[3:5]
    info.append(list(map(int, (a,h,m))))

info.append([0,48,0])
score = [0,0]
time = [[0,0],[0,0]]

for i in range(n):
    score[info[i][0]-1] += 1
    
    if score[0] > score[1]:
        a,b = cal(info[i+1][1],info[i+1][2], info[i][1], info[i][2])
        time[0][0] += a
        time[0][1] += b

    elif score[0] < score[1]:
        a,b = cal(info[i+1][1],info[i+1][2], info[i][1], info[i][2])
        time[1][0] += a
        time[1][1] += b

for i in time:
    if i[1] >= 60:
        i[0] += (i[1]//60)
        i[1] -= (60*(i[1]//60))
        
    for j in range(len(i)):
        if i[j] < 10:
            print('0',i[j],sep='',end='')
        else:
            print(i[j],end='')
        if j==0:
            print(":",end='')
    print()
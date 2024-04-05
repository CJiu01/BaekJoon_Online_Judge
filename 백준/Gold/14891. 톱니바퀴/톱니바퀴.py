import sys
input = sys.stdin.readline

wheel = []
for _ in range(4):
    wheel.append(list(map(int, input().strip())))
    
k = int(input())
direct = []
for _ in range(k):
    direct.append(list(map(int, input().split())))
    

for i in range(k):
    target = direct[i][0]
    move = [0] * 5
    move[target] = direct[i][1]
    
    # 감소
    while target > 1:
        
        if wheel[target-1][6] != wheel[target-2][2]:
            move[target-1] = -move[target]
            target -= 1

        else:
            break
        

    # 증가
    target = direct[i][0]
    while target < 4:
        
        if wheel[target-1][2] != wheel[target][6]:
            move[target+1] = -move[target]
            target += 1
        else:
            break
    
    # wheel 회전
    new = [arr[:] for arr in wheel]
    # print(new)

    for m in range(4):
        # 시계
        if move[m+1] == 1:
            for j in range(7):
                new[m][j+1] = wheel[m][j]
            new[m][0] = wheel[m][7]
        # 반시계
        if move[m+1] == -1:
            for j in range(7):
                new[m][j] = wheel[m][j+1]
            new[m][7] = wheel[m][0]
    
    wheel = new


# 결과
result = 0
if wheel[0][0] == 1:
    result += 1
if wheel[1][0] == 1:
    result += 2
if wheel[2][0] == 1:
    result += 4
if wheel[3][0] == 1:
    result += 8
print(result)
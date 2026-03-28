N = int(input())
cookie = []
for _ in range(N):
    cookie.append(list(input()))
  
x,y = 0,0  
for i in range(N):
    for j in range(N):
        if cookie[i][j] == '*':
            x,y = i,j
            break
    if y!=0:
        break

answer = []
# 왼팔
left_arm = 0
for i in range(y-1,-1,-1):
    if cookie[x+1][i] != '*':
        break
    left_arm+=1
answer.append(left_arm)

# 오른팔
right_arm = 0
for i in range(y+1,N):
    if cookie[x+1][i] != '*':
        break
    right_arm+=1
answer.append(right_arm)

# 허리
waist = 0
for i in range(x+2,N):
    if cookie[i][y] != '*':
        break
    waist+=1
answer.append(waist)

# 왼다리
left_leg = 0
for i in range(x+waist+2,N):
    if cookie[i][y-1] != '*':
        break
    left_leg+=1
answer.append(left_leg)

# 오른다리
right_leg = 0
for i in range(x+waist+2,N):
    if cookie[i][y+1] != '*':
        break
    right_leg+=1
answer.append(right_leg)

print(x+2,y+1)
print(*answer)
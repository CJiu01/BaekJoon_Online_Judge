N = int(input())
cookie = []
for _ in range(N):
    cookie.append(list(input()))
    
def find_heart():
    x,y = 0,0  
    for i in range(N):
        for j in range(N):
            if cookie[i][j] == '*':
                x,y = i,j
                break
        if y!=0:
            break 
    return x,y

def find_length(x,y,dx,dy):
    length = 0 
    while 0 <= x < N and 0 <= y < N and cookie[x][y]=='*':
        length+=1
        x += dx
        y += dy
    return length

x,y = find_heart()
print(x+2, y+1)

left_arm = find_length(x+1,y-1,0,-1)
right_arm = find_length(x+1,y+1,0,1)
waist = find_length(x+2,y,1,0)
left_leg = find_length(x+waist+2,y-1,1,0)
right_leg = find_length(x+waist+2,y+1,1,0)
print(left_arm, right_arm, waist, left_leg, right_leg)
N, M, x, y, K = map(int,input().split())  
arr = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))

dir = [[0,1],[0,-1],[-1,0],[1,0]]
dice = [0]*6

for move in moves:
    dx = x+dir[move-1][0]
    dy = y+dir[move-1][1]
 
    if (dx<0 or dx>=N or dy<0 or dy>=M):
        continue
    
    x, y = dx, dy 
    d0, d1, d2, d3, d4, d5= dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if (move==1):
        dice[1], dice[3], dice[4], dice[5] = d4, d5, d3, d1
    elif (move==2):
        dice[1], dice[3], dice[4], dice[5] = d5, d4, d1, d3
    elif (move==3):
        dice[0], dice[1], dice[2], dice[3] = d1, d2, d3, d0
    elif (move==4):
        dice[0], dice[1], dice[2], dice[3] = d3, d0, d1, d2
        
    if (arr[x][y] == 0):
        arr[x][y] = dice[3]
    else:
        dice[3] = arr[x][y]
        arr[x][y] = 0

    print(dice[1])
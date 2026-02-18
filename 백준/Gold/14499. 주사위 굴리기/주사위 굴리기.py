from collections import deque

def simul(row, col, move):
    if (move==0):
        row.insert(0, row.pop())
        col[1] = row[1]
        col[3] = row[3]
    elif (move==1):
        row.append(row.popleft())
        col[1] = row[1]
        col[3] = row[3]
    elif (move==2):
        col.append(col.popleft())
        row[1] = col[1]
        row[3] = col[3]
    elif (move==3):
        col.insert(0, col.pop())
        row[1] = col[1]
        row[3] = col[3]

N, M, x, y, K = map(int,input().split())  
arr = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))

dir = [[0,1],[0,-1],[-1,0],[1,0]]
row = deque([0]*4)
col = deque([0]*4)
for move in moves:
    dx = x+dir[move-1][0]
    dy = y+dir[move-1][1]
 
    if (dx<0 or dx>=N or dy<0 or dy>=M):
        continue
    
    x, y = dx, dy 
    simul(row, col, move-1)
    if (arr[x][y] == 0):
        arr[x][y] = row[3]
    else:
        row[3] = arr[x][y]
        col[3] = arr[x][y]
        arr[x][y] = 0

    print(row[1])
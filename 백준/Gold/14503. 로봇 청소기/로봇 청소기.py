import sys

dir = [[-1,0],[0,1],[1,0],[0,-1]]
def simul(r, c, d):
    cnt = 0
    while True:
        if (arr[r][c] == 0):
            arr[r][c] = 2
            cnt += 1

        rx, cy = -1,-1
        # 인접한 곳 중 청소 안 된 곳 찾음
        for i in range(1,5):
            tmp_x = r+dir[(d-i)%4][0]
            tmp_y = c+dir[(d-i)%4][1]
            
            if (arr[tmp_x][tmp_y] == 0):
                rx, cy = tmp_x, tmp_y
                d = (d-i)%4
                break

        # 청소 안 된 곳 없는 경우
        if (rx == -1 and cy == -1):
            # 현재 방향 기준으로 후진 
            rx = r + dir[(d+2)%4][0]
            cy = c + dir[(d+2)%4][1]
            if (arr[rx][cy] == 1):
                return cnt
            
        r,c = rx, cy
    
N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(simul(r,c,d))
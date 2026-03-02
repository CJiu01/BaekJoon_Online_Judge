from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
graph = [[0]*N for _ in range(N)]
for _ in range(K):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1

L = int(input())
move = [list(input().split()) for _ in range(L)]

dir = [[-1,0],[0,1],[1,0],[0,-1]]


def snake_game():
    x,y = 0,0 # 초기위치
    time = 0
    length = 1 # 뱀길이
    face = 1
    idx = 0 # move idx 
    q = deque([[x,y]])

    while True:
        time += 1

        dx = x+dir[face%4][0]
        dy = y+dir[face%4][1]
        
        if (0<=dx<N and 0<=dy<N):
            x, y = dx, dy
            if ([x,y] in q):
                return time
            q.append([x,y])
        else:
            return time
        
        if graph[x][y] == 1:
            length += 1
            graph[x][y] = 0
        else:
            q.popleft()
        
        if (idx<L and int(move[idx][0]) == time):
            if move[idx][1]== 'D':
                face += 1
            else:
                face -= 1
            idx+=1

print(snake_game())
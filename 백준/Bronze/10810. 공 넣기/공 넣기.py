import sys
input = sys.stdin.readline

n,m = map(int, input().split())
ball = []
pocket = [0] * n

for i in range(m):
    ball.append(list(map(int, input().split())))
    
for i in range(m):
    start, end = ball[i][0], ball[i][1]
    for j in range(start-1, end):
        pocket[j] = ball[i][2] 
        
print(*pocket[0:], sep=" ")
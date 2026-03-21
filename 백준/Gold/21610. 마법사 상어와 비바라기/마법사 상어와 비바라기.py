import sys
input = sys.stdin.readline

def move(clouds,d,s):
    for cloud in clouds:
        cloud[0] = (cloud[0] + (dir[d][0]*s))%N
        cloud[1] = (cloud[1] + (dir[d][1]*s))%N
        
def rain(clouds):
    for cloud in clouds:
        r,c = cloud[0],cloud[1]
        A[r][c] += 1
        
def magic(clouds):
    for cloud in clouds:
        r,c = cloud[0],cloud[1]
        cnt = 0
        for i in cross:
            dx = r+i[0]
            dy = c+i[1]
            if 0<=dx<N and 0<=dy<N:
                if A[dx][dy]>0:
                    cnt+=1
        A[r][c] += cnt
        
def make_clouds(clouds):
    clouds_set = set(map(tuple, clouds))
    new_clouds = []
    for i in range(N):
        for j in range(N):
            if (i,j) not in clouds_set and A[i][j]>=2:
                A[i][j] -= 2
                new_clouds.append([i,j])
    return new_clouds

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
clouds = [[N-2,0],[N-2,1],[N-1,0],[N-1,1]]
dir = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
cross = [(-1,-1),(-1,1),(1,-1),(1,1)]

for _ in range(M):
    d,s = map(int, input().split())
 
    move(clouds, d-1,s)
    rain(clouds)
    magic(clouds)
    clouds = make_clouds(clouds)
        
print(sum(A[i][j] for i in range(N) for j in range(N)))
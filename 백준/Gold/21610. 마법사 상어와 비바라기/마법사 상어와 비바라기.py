import copy

def move(clouds,d,s):
    for cloud in clouds:
        cloud[0] += (dir[d][0]*s)
        cloud[1] += (dir[d][1]*s)
        cloud[0]%=N
        cloud[1]%=N
        
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
    k = 0
    k_len = len(clouds)
    new_clouds = []
    for i in range(N):
        for j in range(N):
            if k<k_len and clouds[k][0]==i and clouds[k][1]==j:
                k+=1
                continue
            if A[i][j]>=2:
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
    clouds.sort()
    
    rain(clouds)
    magic(clouds)
    clouds = make_clouds(clouds)
        
ans = 0
for i in range(N):
    for j in range(N):
        ans += A[i][j]
        
print(ans)
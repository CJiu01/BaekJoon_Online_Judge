import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def con1(target, likes):
    max = 0
    
    candidate = []
    for i in range(N):
        for j in range(N):
            if pos[i][j] == 0:
                cnt = 0
                for d in range(4):
                    nx = i+dx[d]
                    ny = j+dy[d]
                    
                    if 0<=nx<N and 0<=ny<N:
                        if pos[nx][ny] in likes: # 학생 앉아있고, 그 학생이 likes라면
                            cnt += 1
                if cnt==max:
                    candidate.append([i,j])
                elif cnt>max:
                    candidate = [[i,j]]
                    max = cnt  
    return candidate, max
 
def con2(candidates):
    new_candidates = []
    
    for cdt in candidates:
        cnt = 0;
        x, y = cdt[0], cdt[1]
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<N and 0<=ny<N:
                if pos[nx][ny] == 0:
                    cnt += 1
                
        new_candidates.append([x,y,cnt])
        
    # 빈칸 내림차순 -> 좌표 오름차순으로 정렬
    new_candidates.sort(key = lambda x: (-x[2], x[0], x[1]))
    res = new_candidates[0] 
    
    # target 학생이 앉을 자리 반환
    return res[0], res[1]

def satisfaction_survey(pos, graph):
    score = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            target = pos[i][j]
            likes = graph.get(target)
            
            for d in range(4):
                nx = i+dx[d]
                ny = j+dy[d]
                if 0<=nx<N and 0<=ny<N:
                    if pos[nx][ny] in likes: # 학생 앉아있고, 그 학생이 likes라면
                        cnt += 1
            if cnt==1:
                score+=1
            elif cnt==2:
                score+=10
            elif cnt==3:
                score+=100
            elif cnt==4:
                score+=1000
    return score

N = int(input())

order = []           
graph = {} # 좋아하는 학생 번호
pos = [[0]*N for _ in range(N)] # 학생 자리 배치

for _ in range(N**2):
    tmp = list(map(int, input().split()))
    order.append(tmp[0])
    graph[tmp[0]] = tmp[1:]

for student in order:

    # pos 할당은 여기서만
    target = student
    likes = graph.get(target)
    
    candidates, likes_cnt = con1(target, likes)

    x,y = 0,0
    if len(candidates) > 1:
        x,y = con2(candidates)
    else:
        x,y = candidates[0][0], candidates[0][1]
    pos[x][y] = target  

ans = satisfaction_survey(pos, graph)
print(ans)
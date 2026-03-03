import sys
input = sys.stdin.readline


N, L = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
roads = map
for i in range(N):
    li = []
    for j in range(N):
        li.append(map[j][i])
    roads.append(li)

res = 0

for road in roads:
    
    pre_height = road[0]
    i = 1
    bridge =  [False]*N # 다리 놓았는지 확인
    flag = True
    
    while i<N:
        if (abs(pre_height-road[i])>1):
            break
        
        if (pre_height == road[i]):
            i += 1
        else:
            if (pre_height-road[i]==1): # 앞이 높은 경우
                for k in range(i,i+L):
                    if (k>=N or road[k] != road[i] or bridge[k]):
                        flag = False
                        break
                if not flag:
                    break
                
                # 다리 배열 갱싱
                for k in range(i,i+L):
                    bridge[k] = True
                    
                pre_height = road[i]    
                i = i+L
                     
            else: # 뒤가 높은 경우
                for k in range(i-L,i):
                    if (k<0 or road[k] != road[i-1] or bridge[k]):
                        flag = False
                        break
                if not flag:
                    break
                
                # 다리 배열 갱싱
                for k in range(i-L,i):
                    bridge[k] = True
                    
                pre_height = road[i]
                i = i+1     
    if (i==N):
        res += 1
        
print(res)
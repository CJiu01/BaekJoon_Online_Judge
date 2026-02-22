N, M = map(int, input().split())
medal = [list(map(int, input().split())) for _ in range(N)]
medal.sort(reverse=True, key= lambda x:(x[1],x[2],x[3]))

rank = 1
cnt = 1

for i in range(N):
    
    if (i>0):
        if (medal[i-1][1:] != medal[i][1:]):
            rank += cnt
            cnt = 1
        else:
            cnt += 1
        
    
    if (medal[i][0] == M):
        print(rank)
        break
def bfs(cur, total):
    global cnt
    if (cur==n):
        if(total==s): cnt+=1
        return
        
    bfs(cur+1, total)
    bfs(cur+1, total+arr[cur])
    

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
bfs(0,0)

if (s==0): cnt-=1
print(cnt)
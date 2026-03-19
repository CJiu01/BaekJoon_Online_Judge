def solve(k):
    if k==M:
        print(*arr)
        return
        
    for i in range(1,N+1):
        if not visited[i]:
            arr.append(i)
            visited[i] = True
            solve(k+1)
            arr.pop()
            visited[i] = False
        

N, M = map(int, input().split())
arr = []
visited = [False]*(N+1)
solve(0)
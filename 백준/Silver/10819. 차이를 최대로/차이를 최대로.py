

def back(depth, path, visited, cnt):
    global ans
    if depth==N:
        ans = max(ans, cnt)
        return
    
    for i in range(N):
        if not visited[i]:
            
            visited[i] = True
            path.append(S[i])
            
            diff = 0
            if depth>0:
                diff = abs(path[depth]-path[depth-1])
            cnt += diff
            back(depth+1, path, visited, cnt)
            
            cnt -= diff
            visited[i] = False
            path.pop()
    return

N = int(input())
S = list(map(int, input().split()))
ans = 0
back(0, [], [0]*N, 0)
print(ans)
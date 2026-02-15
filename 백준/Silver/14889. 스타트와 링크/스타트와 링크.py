def back(arr, res, idx, p):
    if (len(res)==2):
        p.append(res)
        return 
    
    for i in range(idx, (N//2)):
        back(arr, res+[arr[i]], i+1, p)

def pair(li):
    p = []
    back(li, [], 0, p)
    return p
    
def calPower(li):
    res = 0
    for pair in li:
        x, y = pair
        res += graph[x][y] + graph[y][x]
    return res

def power(team):
    other = [i for i in range(N) if i not in team]
    a = pair(team) # team으로 만들 수 있는 쌍
    b = pair(other) # other로 만들 수 있는 쌍
    aPower = calPower(a)
    bPower = calPower(b)
    diff = abs(aPower-bPower)
    return diff
    
def dfs(team, idx):
    global answer
    if(len(team)==(N//2)):
        answer = min(answer, power(team))
        
    for i in range(idx, N):
        dfs(team+[i], i+1)
        
N = int(input())    
graph = [list(map(int, input().split())) for _ in range(N)]
 
team = []
answer = 100
dfs(team, 0)
print(answer)
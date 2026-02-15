from itertools import combinations

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
members = list(range(n))
ans = 1e9

def sum_score(arr):
    total = 0
    for i,j in combinations(arr, 2):
        total += graph[i][j] + graph[j][i]
    return total
    


for team_a in combinations(members, n//2):
    team_b = list(set(members) - set(team_a))
    
    ans = min(ans, abs(sum_score(team_a)-sum_score(team_b)))
    if ans==0:
        break
    
print(ans)
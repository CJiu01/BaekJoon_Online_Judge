import sys
input = sys.stdin.readline

def calculate_dist(p1, p2):
    dist = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    return dist

N = int(input())
check = [list(map(int, input().split())) for _ in range(N)]

dist = [0]
whole_dist = 0
for i in range(1,N):
    d = calculate_dist(check[i],check[i-1])
    dist.append(d)
    whole_dist += d


ans = 1e9
for i in range(1,N-1):
    tmp = whole_dist - dist[i] - dist[i+1] + calculate_dist(check[i+1], check[i-1])
    ans = min(ans, tmp)
    
print(ans)
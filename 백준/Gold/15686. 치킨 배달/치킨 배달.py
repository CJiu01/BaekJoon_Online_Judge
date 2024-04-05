import sys
import itertools
input = sys.stdin.readline

n,m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))
    
# 치킨집 찾기
chicken = []
house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i,j])
        if city[i][j] == 2:
            chicken.append([i,j])

chicken_comb = list(itertools.combinations(chicken, m))

min_distance = 1_000_000_000
for i in chicken_comb:
    distance = 0
    
    for j in house:
        if min_distance < distance:
            break
        temp = []
        for k in range(m):
            temp.append(abs(i[k][0] - j[0]) + abs(i[k][1] - j[1]))
            
        distance += min(temp)
    
    if min_distance > distance:
        min_distance = distance
        
print(min_distance)
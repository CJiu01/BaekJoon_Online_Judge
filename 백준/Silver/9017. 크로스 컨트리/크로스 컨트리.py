from collections import Counter

T = int(input())
for _ in range(T):

    N = int(input())
    numbers = list(map(int, input().split()))
    teams = dict(Counter(numbers))

    pass_teams = {}
    for k,v in teams.items():
        if v==6:
            pass_teams[k] = [0,0,0]

    pass_teams_name = list(pass_teams.keys())

    score = 1
    for i in range(N):
        if numbers[i] in pass_teams_name:
            if pass_teams[numbers[i]][1]==4:
                pass_teams[numbers[i]][2] = score 
            elif pass_teams[numbers[i]][1]<4:
                pass_teams[numbers[i]][0] += score
            
            pass_teams[numbers[i]][1] += 1
            score+=1

    res = []
    for k,v in pass_teams.items():
        res.append([v[0],v[2],k])
        
    res.sort(key=lambda x:(x[0],x[1]))
    print(res[0][2])
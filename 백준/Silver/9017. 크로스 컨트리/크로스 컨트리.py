from collections import Counter

T = int(input())
for _ in range(T):

    N = int(input())
    l = list(map(int, input().split()))
    counter = Counter(l)
    dic = {}
    score = 1
    
    for i in range(N):
        if counter[l[i]] == 6:
            if l[i] in dic:
                dic[l[i]].append(score)
            else:
                dic[l[i]] = [score]
            score+=1
            
    print(sorted(dic, key=lambda x: (sum(dic[x][0:4]), dic[x][4]))[0])
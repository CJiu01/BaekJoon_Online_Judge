import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = dict()

for _ in range(N):
    word = input().rstrip()
    
    if (len(word)>=M):
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
            
ans = sorted(dic.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))
for x,y in ans:
    print(x)
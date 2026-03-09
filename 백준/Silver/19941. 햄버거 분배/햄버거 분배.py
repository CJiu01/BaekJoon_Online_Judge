import sys
input = sys.stdin.readline
N, K = map(int, input().split())
s = input().rstrip()
hambur = [False]*N
people = []

for i in range(len(s)):
    if s[i] == 'H':
        hambur[i] = True
    else:
        people.append(i)

ans = 0

for p in people:
    for j in range(p-K,p+K+1):
        if 0<=j<N and hambur[j]:
            ans+=1
            hambur[j] = False
            break
print(ans)
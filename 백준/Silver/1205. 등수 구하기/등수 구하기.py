import sys
input = sys.stdin.readline

N, new_score, P = map(int, input().split())
scores = []
if N > 0:
    scores = list(map(int, input().split()))

rank = 1
same = 0
for s in scores:
    if s > new_score:
        rank += 1
    elif s == new_score:
        same += 1

if not scores and P > 0:
    print(1)
elif rank <= P and rank + same <= P: 
    print(rank)
else:
    print(-1)
import sys
input = sys.stdin.readline


N, new_score, P = map(int, input().split())
scores = []
if N > 0:
    scores = list(map(int, input().split()))
    
if N==0:
    print(1)
else:
    if N==P and new_score <= scores[-1]:
        print(-1)
    else:
        rank = 1
        for i in scores:
            if i>new_score:
                rank+=1
        print(rank)
    
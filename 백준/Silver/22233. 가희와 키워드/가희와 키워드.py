import sys
input = sys.stdin.readline

N, M = map(int, input().split())
keyword = set()
for _ in range(N):
    keyword.add(input().rstrip())
    
for _ in range(M):
    for word in input().rstrip().split(','):
        keyword.discard(word)
    print(len(keyword))
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

a = set()
count = 0

for _ in range(N):
  a.add(input().rstrip())

for _ in range(M):
  if input().rstrip() in a:
    count += 1

print(count)
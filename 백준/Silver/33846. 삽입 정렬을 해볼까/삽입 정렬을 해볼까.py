import sys
input = sys.stdin.readline

n, t = map(int, input().split())
l = list(map(int, input().split()))
print(*(sorted(l[:t])+l[t:]))
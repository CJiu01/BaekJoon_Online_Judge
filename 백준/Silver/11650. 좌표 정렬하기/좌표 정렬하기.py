import sys
input = sys.stdin.readline

n = int(input())
arr = [[]*2 for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int,input().split()))
arr.sort()

for i in range(n):
    print(arr[i][0], arr[i][1])
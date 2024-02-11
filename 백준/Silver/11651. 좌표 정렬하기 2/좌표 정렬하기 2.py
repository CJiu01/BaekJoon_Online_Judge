import sys
input = sys.stdin.readline

n = int(input())
arr = [[]*2 for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int,input().split()))
    
arr.sort(key = lambda x: (x[1], x[0]))

for i in range(n):
    print(arr[i][0], arr[i][1])
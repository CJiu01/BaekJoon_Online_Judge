import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
arr = list(map(int, input().split()))

arr.sort()    
interval = [arr[i+1]-arr[i] for i in range(N-1)]
interval.sort(reverse=True)
res = sum(interval[K-1:])
print(res)
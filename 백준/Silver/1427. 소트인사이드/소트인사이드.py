import sys
input = sys.stdin.readline

arr = list(input())
arr.sort(reverse=True)
print(int(''.join(arr)))

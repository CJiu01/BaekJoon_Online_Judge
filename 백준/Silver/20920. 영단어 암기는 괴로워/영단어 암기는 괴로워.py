from collections import Counter
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

for _ in range(N):
    word = input().rstrip()
    if (len(word)>=M):
        arr.append(word)
        
dic = Counter(arr)
arr = []
for key,value in dic.items():
    arr.append((value, len(key), key))
arr.sort(key=lambda x: (-x[0],-x[1],x[2]))

print(*(row[2] for row in arr), sep='\n')
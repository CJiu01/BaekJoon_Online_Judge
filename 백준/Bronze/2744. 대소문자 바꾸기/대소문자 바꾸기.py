import sys
input = sys.stdin.readline


str = input().strip()
res = ''
for i in str:
    if ord(i)<=90:
        res += i.lower()
    else:
        res += i.upper()
print(res)
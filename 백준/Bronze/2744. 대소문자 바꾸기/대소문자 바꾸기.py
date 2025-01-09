import sys
input = sys.stdin.readline


str = input().strip()
res = ''
for i in str:
    if i<chr(90):
        res += chr(ord(i)+32)
    else:
        res += chr(ord(i)-32)
        
print(res)
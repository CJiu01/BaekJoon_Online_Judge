import sys
input = sys.stdin.readline

def solution(user,q,s):
    a = user[0]
    if a==1:
        s.append(user[1])
        q.append(user)
    elif a==2:
        q.append([2,s.pop()])
    elif a==3:
        i = user[1]
        while i>0:
            k = q.pop()
            if k[0]==1:
                s.pop()
            else:
                s.append(k[1])
            i-=1
    elif a==4:
        print(len(s))
    else:
        print(s[-1] if s else -1)
    
n = int(input())
q = []
s = []
for _ in range(n):
    user = list(map(int, input().split()))
    solution(user,q,s)
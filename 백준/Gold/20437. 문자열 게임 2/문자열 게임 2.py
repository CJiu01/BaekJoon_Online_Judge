import sys
input=sys.stdin.readline
T = int(input())
for _ in range(T):
    str = input().rstrip()
    k=int(input())
    al = [[] for _ in range(26)]
    max_len = 0
    min_len = 10001

    for i in range(len(str)):
        s = ord(str[i])-97
        al[s].append(i)
        
        length = len(al[s])
        if length>=k:
            tmp = len(str[al[s][length-k]:al[s][-1]+1])
            max_len = max(max_len, tmp)
            min_len = min(min_len, tmp)

    if max_len == 0:
        print(-1)
    else:
        print(min_len, max_len)
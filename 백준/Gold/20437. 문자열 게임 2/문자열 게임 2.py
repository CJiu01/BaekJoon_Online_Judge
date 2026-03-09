T = int(input())
for _ in range(T):
    str = input()
    k=int(input())
    pos = [[] for _ in range(26)]
    max_len = 0
    min_len = 10001

    for i,ch in enumerate(str):
        idx = ord(str[i])-97
        pos[idx].append(i)
        
        if len(pos[idx])>=k:
            start = pos[idx][-k]
            tmp = i - start + 1
            max_len = max(max_len, tmp)
            min_len = min(min_len, tmp)

    if max_len == 0:
        print(-1)
    else:
        print(min_len, max_len)
S = input()
zero_cnt = 0
one_cnt = 0
for s in S:
    if s=='0':
        zero_cnt += 1
    else:
        one_cnt += 1
        
zero_cnt //= 2
one_cnt //= 2

new = ''
for i in range(len(S)):
    if one_cnt == 0:
        new += S[i:]
        break
    
    if S[i]=='1':
        one_cnt -= 1
    else:
        new += S[i]

new = new[::-1]
ans = ''

for i in range(len(new)):
    if zero_cnt == 0:
        ans += new[i:]
        break
    
    if new[i]=='0':
        zero_cnt -= 1
    else:
        ans += new[i]

ans = ans[::-1]
print(ans)
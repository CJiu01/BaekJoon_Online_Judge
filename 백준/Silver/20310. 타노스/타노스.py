S = list(input().strip())
a = S.count('0') // 2
b = S.count('1') // 2

for i in range(len(S)):
    if b>0 and S[i]=='1':
        S[i] = ''
        b -= 1
        
for i in range(len(S)-1,-1,-1):
    if a>0 and S[i]=='0':
        S[i] = ''
        a -= 1
print(''.join(S))
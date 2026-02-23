s = input()
cnt_a = 0
len_s = len(s)
for i in range(len_s):
    if s[i]=='a':
        cnt_a += 1     
res = 1000
for i in range(len_s):
    if s[i]=='a':
        change = 0
        for j in range(i+1, i+cnt_a):
            if s[j%len_s]!='a':
                change+=1
        
        res = min(res, change)
        
print(res if res!=1000 else 0)

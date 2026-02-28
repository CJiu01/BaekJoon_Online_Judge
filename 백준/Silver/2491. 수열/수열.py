n = int(input())
data = list(map(int, input().split()))

b_ans = 1 #증가
s_ans = 1 #감소

max_ans = 1
for i in range(1,n):
    if data[i-1]==data[i]:
        b_ans+=1
        s_ans+=1
    elif data[i-1]>data[i]:
        s_ans+=1
        b_ans=1
    else:
        b_ans+=1
        s_ans=1
    max_ans = max(max_ans,b_ans,s_ans)
print(max_ans)
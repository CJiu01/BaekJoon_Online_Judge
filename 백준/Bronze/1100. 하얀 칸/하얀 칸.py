chase = []
for i in range(8):
    chase.append(list(input()))
    
    
count = 0
flag = 2



for i in range(8):
    flag = i%2
    for j in range(8):
        if (j%2 == flag) & (chase[i][j]=='F'):
            count+=1
print(count)
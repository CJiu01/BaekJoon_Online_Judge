def back(row, isused1, isused2, isused3):
    global cnt 
    if(row == N):
        cnt +=1
        return

    for i in range(N):
        if (isused1[i] or isused2[row+i] or isused3[row-i+N-1]):
            continue
        isused1[i] = True
        isused2[row+i] = True
        isused3[row-i+N-1] = True
        back(row+1, isused1, isused2, isused3)
        isused1[i] = False
        isused2[row+i] = False
        isused3[row-i+N-1] = False
            
N = int(input())
cnt = 0
isused1 = [False]*N
isused2 = [False]*((N-1)*2+1)
isused3 = [False]*((N-1)*2+1)

back(0, isused1, isused2, isused3)
print(cnt)
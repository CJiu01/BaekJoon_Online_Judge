arr = [False]*10001

for i in range(1,10001):
    
    if arr[i] == False:
        sum = i
        idx = i
        while True:
            for number in str(idx):
                sum += int(number)
                
            if sum<=10000:
                arr[sum] = True
                idx = sum
            else:
                break
                    
for i in range(1,10001):
    if arr[i]==False:
        print(i)
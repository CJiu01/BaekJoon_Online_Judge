n = int(input())
num = list(map(int, input().split()))
num.sort()

m = int(input())
target = list(map(int, input().split()))


def binarysearch(i):
    start = 0
    end = n-1
    
    while(start <= end):
        mid = (start+end) //2
        
        if(num[mid] == i):
            return 1
        elif(num[mid] > i):
            end = mid-1
        elif(num[mid] < i):
            start = mid+1
            
    return 0

for i in range(m):
    print(binarysearch(target[i]))
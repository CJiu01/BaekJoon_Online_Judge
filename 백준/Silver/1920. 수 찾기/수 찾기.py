import sys

N = int(input())
arrlist = list(map(int,sys.stdin.readline().split()))
M = int(input())
solutionlist = list(map(int,sys.stdin.readline().split()))
arrlist.sort()

def binarySearch(target):
    start = 0
    end = N-1

    while(start <= end):
        mid = (start+end) // 2

        if(arrlist[mid] == target):
            return 1
        elif(arrlist[mid] > target):
            end = mid-1
        elif(arrlist[mid] < target):
            start = mid+1
    
    return 0

for i in range(M):
    print(binarySearch(solutionlist[i]))

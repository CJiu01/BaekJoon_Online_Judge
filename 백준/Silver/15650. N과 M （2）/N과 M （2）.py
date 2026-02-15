def back(arr, idx):
    if(len(arr)==M):
        print(*arr)
        return
    
    for i in range(idx, N+1):
        back(arr+[i], i+1)
        
        
N, M = map(int, input().split())
arr = []
back(arr, 1)

def make_gifts(arr, gifts, f):
    
    for gift in gifts:
        a,b = gift.split(' ')
        arr[f[a]][f[b]] +=1
    
    return

def cal_index(n,arr):
    indexed = [0]*n
    for i in range(n):
        indexed[i] = sum(arr[i]) - sum(k[i] for k in arr)
    return indexed

def cal_received(n, arr, indexed):
    received = [0]*n
    for i in range(n):
        for j in range(n):
            if arr[i][j]>arr[j][i]:
                received[i] += 1
            elif arr[i][j]==arr[j][i]:
                if indexed[i]>indexed[j]:
                    received[i] += 1

    return received

def solution(friends, gifts):    
    n = len(friends)
    arr = [[0]*n for _ in range(n)]
    f = {v:i for i,v in enumerate(friends)}
        
    make_gifts(arr, gifts, f)
    indexed = cal_index(n,arr)
    answer = cal_received(n,arr,indexed)
    
    return max(answer)
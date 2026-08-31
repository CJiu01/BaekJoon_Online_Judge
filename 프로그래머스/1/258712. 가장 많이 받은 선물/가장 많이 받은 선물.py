
def make_gifts(arr, gifts, name_order):
    
    for gift in gifts:
        a,b = gift.split(' ')
        arr[name_order[a]][name_order[b]] +=1
    
    return

def cal_index(n,arr):
    indexed = [0]*n
    for i in range(n):
        indexed[i] += sum(arr[i])
        for j in range(n):
            indexed[i] -= arr[j][i]

    return indexed

def cal_received(n, arr, indexed):
    received = [0]*n

    # ([i][j]!=0 or [j][i]!=0) and [i][j]!=[j][i])
    for i in range(n):
        for j in range(i+1,n):
            target = -1

            
            if ((arr[i][j]!=0 or arr[j][i]!=0) and arr[i][j]!=arr[j][i]):
                # 큰사람이 받기
                target = i if arr[i][j]>arr[j][i] else j

            else:
                if indexed[i]>indexed[j]:
                    target = i
                elif indexed[i]<indexed[j]:
                    target = j
                
            if target!=-1:
                received[target] +=1

    return received

def solution(friends, gifts):
    answer = 0
    
    n = len(friends)
    arr = [[0]*n for _ in range(n)]
    name_order = {}
    for i in range(len(friends)):
        name_order[friends[i]] = i
        
    make_gifts(arr, gifts, name_order)
    indexed = cal_index(n,arr)
    res = cal_received(n,arr,indexed)
    answer = max(res)
    
    return answer

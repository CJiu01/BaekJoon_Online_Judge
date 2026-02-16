import copy

def checkLongCnt(list):
    maxCnt = 0
    #hori
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if (list[i][j] == list[i][j+1]):
                cnt += 1
                maxCnt = max(maxCnt, cnt)
            else:
                cnt = 1
    #ver
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if (list[j][i] == list[j+1][i]):
                cnt += 1
                maxCnt = max(maxCnt, cnt)
            else:
                cnt = 1
    return maxCnt
    
def swap(arr):
    global res
    #hori
    for i in range(N):
        for j in range(N-1):
            if (arr[i][j] == arr[i][j+1]):
                continue
            changed = copy.deepcopy(arr)
            tmp = changed[i][j]
            changed[i][j] = changed[i][j+1]
            changed[i][j+1] = tmp
            res = max(res, checkLongCnt(changed))
    #ver
    for i in range(N):
        for j in range(N-1):
            if (arr[j][i] == arr[j+1][i]):
                continue
            changed = copy.deepcopy(arr)
            tmp = changed[j][i]
            changed[j][i] = changed[j+1][i]
            changed[j+1][i] = tmp
            res = max(res, checkLongCnt(changed))

N = int(input())
arr = [list(input()) for _ in range(N)]
res = 0

swap(arr)
print(res)
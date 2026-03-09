from collections import Counter


def oper_R(arr):
    trans_arr = []
    for j in range(len(arr)):
        counter = Counter(i for i in arr[j] if i!=0)

        count_vec = []
        for a,b in counter.items():
            count_vec.append([a,b])
            
        count_vec.sort(key= lambda x: (x[1],x[0]))
        trans_arr.append(count_vec)
    return trans_arr

def oper_C(arr):
    trans_arr = []
    
    for i in range(len(arr[0])):
        tmp = []
        for j in range(len(arr)):
            tmp.append(arr[j][i])
        counter = Counter(k for k in tmp if k!=0)
        
        count_vec = []
        for a,b in counter.items():
            count_vec.append([a,b])
            
        count_vec.sort(key= lambda x: (x[1],x[0]))
        trans_arr.append(count_vec)
    return trans_arr
        

r, c, k = map(int, input().split())
r,c = r-1,c-1
arr = [list(map(int, input().split())) for _ in range(3)]
time = 0
row, col = 3,3
oper = True


while time <= 100:
    
    row = len(arr)-1
    col = len(arr[0])-1
    
    # # [r][c] == k 확인
    if r<=row and c<=col:
        if arr[r][c] == k:
            break
    time += 1
   
    new = []
    # 행/열 개수 비교
    if row>=col:
        new = oper_R(arr)
    else:
        new = oper_C(arr)

    flat = []
    for ro in new:
        temp = []
        for a, b in ro:
            temp.extend([a, b])
        flat.append(temp)

    max_len = max(len(r) for r in flat)

    for ro in flat:
        ro.extend([0] * (max_len - len(ro)))
       
    if row<col: 
        tmp = [[0]*len(flat) for _ in range(max_len)]
        for i in range(len(flat)):
            for j in range(max_len):
                tmp[j][i] = flat[i][j]
        flat = tmp[:]
    arr = flat[:]
    
if time<=100:
    print(time)
else:
    print(-1)
def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(e) for e in list_of_tuples]

def find(l, target):
    res = []
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] == target:
                res.append((i,j))
                
    return res

def solution(key, lock):
    n = len(lock)
    m = len(key)
    keyed = find(key, 1)
    locked = find(lock ,0)
    
    for _ in range(4):
        i=-m+1
        
        while i<n:
            j = -m+1
            while j<n:
                tkey = keyed[:]
                for k in range(len(tkey)):
                    tkey[k] = (tkey[k][0]+i, tkey[k][1]+j)

                # N*N영역 내의 key만 필터
                nkey = []
                flag = True
                for k in tkey:
                    if 0<=k[0]<n and 0<=k[1]<n:
                        if lock[k[0]][k[1]]!=1:
                            nkey.append(k)
                        else:
                            flag = False
                            break
                        
                if flag and nkey==locked:
                    return True
                j+=1
            i+=1 

        key = rotated(key)
        keyed = find(key, 1)
    
    return False
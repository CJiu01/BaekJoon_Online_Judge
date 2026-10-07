def solution(topping):
    answer = 0
    n = len(topping)
    start, end, mid = 0, n, 0
     
    while start<=end:
        mid = (start+end)//2
        kind_a = len(set(topping[0:mid]))
        kind_b = len(set(topping[mid:n]))
        if kind_a == kind_b:
            answer+=1
            break
        elif kind_a > kind_b:
            end = mid-1
        else:
            start = mid+1
    
    if answer==0:
        return 0
    
    test_kind_A = [0]*10001
    test_kind_B = [0]*10001
    for i in range(0, mid):
        test_kind_A[topping[i]] += 1
    
    for i in range(mid, n):
        test_kind_B[topping[i]] += 1
    
    tmp_A = test_kind_A.copy()
    tmp_B = test_kind_B.copy()
    for i in range(mid-1,-1,-1):
        if tmp_A[topping[i]]-1==0 or tmp_B[topping[i]]+1==1:
            break
        tmp_A[topping[i]]-=1
        tmp_B[topping[i]]+=1
        answer+=1

    for i in range(mid,n):
        if test_kind_A[topping[i]]+1==1 or test_kind_B[topping[i]]-1==0:
            break
        test_kind_A[topping[i]]+=1
        test_kind_B[topping[i]]-=1
        answer+=1

    return answer
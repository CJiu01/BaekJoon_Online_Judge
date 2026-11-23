def solution(n, q, m):
    q.sort()
    start, end = m//n, q[-1]
    
    while start<=end:
        mid = (start+end)//2
        given = [0]*n
        for i in range(n):
            if mid>=q[i]:
                given[i] = q[i]
            else:
                given[i] = mid
        total = sum(given)
        if total==m:
            return given[-1]
        elif total>m:
            end = mid-1
        else:
            start = mid+1
    return end if end<q[-1] else q[-1]

n = int(input())
q = list(map(int, input().split()))
m = int(input())
print(solution(n, q, m))
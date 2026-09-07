from collections import deque

def sliding_min(arr, k):
    dq = deque()
    n = len(arr)
    res = [None]*(n-k+1)
    
    for idx in range(n):
        while dq and dq[-1][1]>=arr[idx]:
            dq.pop()
        dq.append([idx,arr[idx]])
        if dq[0][0]<=idx-k:
            dq.popleft()
        if idx >= k-1:
            res[idx-k+1] = dq[0][1]

    return res
    
def solution(m, n, h, w, drops):
    answer = []
    INF = 500000
    graph = [[INF]*n for _ in range(m)]
    
    for i,d in enumerate(drops):
        graph[d[0]][d[1]] = i
        
    row_min = [sliding_min(arr, w) for arr in graph]
    
    col = [[row_min[i][j] for i in range(len(row_min))] for j in range(len(row_min[0]))]
    final_min = [sliding_min(arr, h) for arr in col]
    
    turn = -1
    for i in range(len(final_min[0])):
        for j in range(len(final_min)):
            if final_min[j][i] == INF:
                return [i,j]
            if turn<final_min[j][i]:
                answer = [i,j]
                turn = final_min[j][i]

    return answer

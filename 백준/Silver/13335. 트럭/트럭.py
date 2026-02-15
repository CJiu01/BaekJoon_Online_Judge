from collections import deque

n, w, L = map(int, input().split())
weight = list(map(int, input().split()))
bridge = deque([0]*w)

i = 0
time = 0
while True:
    
    bridge.popleft()
    
    if (i<n):
        if (sum(bridge) + weight[i] <= L):
            bridge.append(weight[i])
            i+=1
            time+=1
        else:
            bridge.append(0)
            time += 1
    else:
        bridge.append(0)
        time += 1
        
    if (sum(bridge)==0):
        print(time)
        break
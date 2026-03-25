import sys

def back(depth, arr, start):
    if depth==6:
        print(*arr)
        return
    
    for i in range(start, k):
        back(depth+1, arr+[S[i]], i+1)
        
    return

while True:
    str = sys.stdin.readline().rstrip()
    if str=='0':
        break
    
    k, *S = map(int, str.split())
    a = []
    back(0, a, 0)
    print()
import sys

def back(depth, start, path):
    if depth==6:
        print(*path)
        return
    
    for i in range(start, k):
        path.append(S[i])
        back(depth+1, i+1, path)
        path.pop()
        
    return

while True:
    line = sys.stdin.readline().split()
    if line[0]=='0':
        break
    
    k = int(line[0])
    S = list(map(int, line[1:]))
    
    back(0, 0, [])
    print()
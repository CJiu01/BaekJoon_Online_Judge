import sys

while True:
    user = sys.stdin.readline().rstrip('\n')
    
    if not user:
        break

    arr = [0]*4
    
    for i in user:
        target = ord(i)
        if 48<=target<=57:
            arr[2]+=1
        elif 65<=target<=90:
            arr[1]+=1
        elif 97<=target<=122:
            arr[0]+=1
        else:
            arr[3]+=1
    print(*arr)
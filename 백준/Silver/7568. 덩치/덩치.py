import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split(' '))))
    
grade = [0]*N
for i in range(N):
    for j in range(i+1,N):
        if arr[i][0] < arr[j][0]:
            if arr[i][1] < arr[j][1]:
                grade[i] += 1
        elif arr[i][0] > arr[j][0]:
            if arr[i][1] > arr[j][1]:
                grade[j] += 1
for i in grade:
    print(i+1,end=' ')
print('')

# rank = [sorted(grade, reverse=True).index(i) for i in grade]

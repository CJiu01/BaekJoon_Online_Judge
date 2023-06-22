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

# 이차원 배열 한 줄로 받기
# arr = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)]

# sorted 함수로 순위 매기기
# rank = [sorted(grade, reverse=True).index(i) for i in grade]

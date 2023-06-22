import sys

number = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())
operand = str(a*b*c)

for i in operand:
    number[int(i)] += 1
    
for i in number:
    print(number[i])

# 입력 한 번에 받기
# a,b,c = (int(sys.stdin.readline()) for _ in range(3))

# 문자열 count 함수 써서 계산하기
# for i in range(10):
#     print(operand.count(str(i)))
    

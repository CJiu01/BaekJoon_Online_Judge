import sys
input = sys.stdin.readline

def man(num):
    i = num-1
    while i < cnt_switch:
        turn(i)
        i += num

def woman(num):
    left = right = num-1
    tl = num-2
    tr = num
    
    while tl >= 0 and tr < cnt_switch:
        if switch[tl] == switch[tr]:
            left = tl
            right = tr
        else:
            break   
        tl -= 1
        tr += 1
        
    for i in range(left, right+1):
        turn(i)
    
def turn(i):
    if switch[i] == 0:
        switch[i] = 1
    else:
        switch[i] = 0

cnt_switch = int(input())
switch = list(map(int, input().split()))

cnt_student = int(input())
student = []
for _ in range(cnt_student):
    student.append(list(map(int, input().split())))
    
for i in range(cnt_student):
    if student[i][0] == 1:
        man(student[i][1])
    else:
        woman(student[i][1])
        
for i in switch: print(i)
n = int(input())
ball = list(input())
color = ball[0]
ans = 0

def move(target, arr):
    start_color = ball[0]
    end_color = ball[n-1]

    target_start = arr[0] if start_color==target else 0
    target_end = arr[-1] if end_color==target else 0
    target_ans = sum(arr)
    if (target_start==0 and target_end==0):
        pass
    elif (target_start > target_end):
        target_ans -= arr[0]
    else:
        target_ans -= arr[-1]

    return target_ans

red_ball = []
blue_ball = []
idx = 0
cnt=1

for i in range(1,n):
    if(ball[i-1]==ball[i]):
        cnt+=1
        
    else:
        if(color=='R'):
            red_ball.append(cnt)
            color='B'
            cnt=1
        else:
            blue_ball.append(cnt)
            color='R'
            cnt=1
    if(i==n-1):
        if(color=='R'):
            red_ball.append(cnt)
            color='B'
            cnt=1
        else:
            blue_ball.append(cnt)
            color='R'
            cnt=1
                
if(n==1 or len(set(ball))==1): print(0)
else: print(min(move('R', red_ball),move('B', blue_ball)))
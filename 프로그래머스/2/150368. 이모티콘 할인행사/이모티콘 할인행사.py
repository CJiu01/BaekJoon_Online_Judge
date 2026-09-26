def buy(m, sale, moeny, users, k):
    for (i,v) in enumerate(users):
        if v[0]<=sale:
            moeny[i][k] = m
        else:
            moeny[i][k] = 0

def back(k, sales, moeny, emoticons, users, res):
    if(k>=len(emoticons)):
        # 가입자, 금액 세기
        cnt_new,cnt_moeny = 0,0
        
        for (u,mo) in zip(users, moeny):
            s = sum(mo)
            if s>=u[1]:
                cnt_new += 1 
            else:
                cnt_moeny += s
        res.append([cnt_new, cnt_moeny])
        return
    
    for i in range(1,5):
        sales[k] = i*10
        m = emoticons[k]*(100-sales[k])//100 # 할인 적용된 금액
        buy(m, sales[k], moeny, users, k)
        back(k+1, sales, moeny, emoticons, users, res)

def solution(users, emoticons):
    res = []
    money = [[0]*len(emoticons) for _ in range(len(users))]
    back(0, [0]*len(emoticons), money, emoticons, users, res)
    res.sort(reverse=True)
    
    return res[0]
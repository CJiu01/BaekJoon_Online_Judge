from itertools import combinations

def game(buy_hint_stage, cost, hint):
    n = len(cost)
    hint_cnt = [0]*n
    money = 0
    
    # 구매한 힌트권 몇 장인지 세팅
    for i in buy_hint_stage:
        h = hint[i]
        money += h[0]
        for j in range(1,len(h)):
            hint_cnt[h[j]-1] += 1
    
        
    # 힌트권에 따라 스테이지 해결
    for i in range(n):
        if len(cost[i])<=hint_cnt[i]:
            money += cost[i][-1]
        else:
            money += cost[i][hint_cnt[i]]
    
    return money

def solution(cost, hint):
    answer = 10000000
    n = len(hint)
    
    buy_hint = []
    li = [j for j in range(n)]

    for i in range(n+1):
        buy_hint.extend(list(combinations(li, i)))
    
    for buy in buy_hint:
        m = game(buy, cost, hint)
        if m!=-1:
            answer = min(answer, m)

    return answer
def solution(wallet, bill):
    answer = 0
    
    while True:
        w_wallet = min(wallet)
        h_wallet = max(wallet)
        w_bill = min(bill)
        h_bill = max(bill)
        
        if w_wallet>=w_bill and h_wallet>=h_bill:
            return answer
        bill = [h_bill//2, w_bill]
        answer+=1
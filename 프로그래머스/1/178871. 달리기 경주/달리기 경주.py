def solution(players, callings):
    
    ctn = {}
    
    for i in range(len(players)):
        ctn[players[i]] = i
        
    for i in callings:
        winner_n = ctn[i]-1 
        loser_n = ctn[i] 
        
        players[winner_n], players[loser_n] = players[loser_n], players[winner_n]
        ctn[players[winner_n]], ctn[players[loser_n]] = winner_n, loser_n
    
    return players
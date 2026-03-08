next = [
1,2,3,4,5,6,7,8,9,10,
11,12,13,14,15,16,17,18,19,20,
32,
22,23,24,25,26,20,
28,24,
30,31,24,
32
]

score_board = [
    0,2,4,6,8,10,12,14,16,18,
    20,22,24,26,28,30,32,34,36,38,
    40,
    13,16,19,25,30,35,
    22,24,
    28,27,26,
    0
]

blue = [-1]*33

blue[5] = 21   # 10 → 13
blue[10] = 27  # 20 → 22
blue[15] = 29  # 30 → 28


ans=0
horse=[0,0,0,0]

def move(node, dice):
    if blue[node] != -1:
        node = blue[node]
        dice -= 1
        
    else:
        node = next[node]
        dice -= 1
        
    while dice>0 and node!=32:
        node = next[node]
        dice -= 1
        
    return node
  
def dfs(turn, score):
    global ans 
    if turn == 10:
        ans = max(ans, score)
        return
    
    for i in range(4):
        cur = horse[i]
        if cur==32:
            continue
        
        nxt = move(cur, dice[turn])
        
        if nxt!=32 and nxt in horse:
            continue
        
        horse[i] = nxt
        dfs(turn+1, score+score_board[nxt])
        horse[i] = cur
        
dice = list(map(int,input().split()))
dfs(0,0)
print(ans)
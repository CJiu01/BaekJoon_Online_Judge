import sys
input = sys.stdin.readline

def solution():
    
    cnt = 0
    bingo_count = 0
    
    for i in range(25):
        find_num_location(speak[i])
        cnt += 1

        bingo_count = check_bingo()
        if bingo_count >= 3:
            return cnt

def find_num_location(num):
    global bingo
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                bingo[i][j] = 1
                return 
            
def check_bingo():
    count = 0
    cnt_inter = 0
    cnt_inter_opp = 0

    for i in range(5):
        cnt_row = 0
        cnt_col = 0
        for j in range(5):
            if bingo[i][j] == 1:
                cnt_row += 1
            if bingo[j][i] == 1:
                cnt_col += 1
        if cnt_row == 5:
            count += 1
        if cnt_col == 5:
            count += 1
        if bingo[i][i] == 1:
            cnt_inter += 1
        if bingo[i][4-i] == 1:
            cnt_inter_opp += 1

    if cnt_inter == 5:
        count += 1
    if cnt_inter_opp == 5:
        count += 1

    return count

board = []
for _ in range(5):
    board.append(list(map(int, input().split())))
    
speak = []
for _ in range(5):
    speak.append(list(map(int, input().split())))     
speak = [element for row in speak for element in row]
  
bingo = [[0]*5 for _ in range(5)]
print(solution())

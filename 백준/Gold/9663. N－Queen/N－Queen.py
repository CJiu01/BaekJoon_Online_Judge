import sys
input = sys.stdin.readline

count = 0
board = [0] * 15

def promise(cdx):
    for i in range(0, cdx):
        if board[i] == board[cdx] or (cdx-i) == abs(board[i]-board[cdx]):
            return False
    return True

def nqueen(cdx):
    global count

    if cdx == n:
        count += 1
        return 
    
    for i in range(n):
        board[cdx] = i
        if(promise(cdx)):
            nqueen(cdx+1)

n = int(input())
nqueen(0)
print(count)
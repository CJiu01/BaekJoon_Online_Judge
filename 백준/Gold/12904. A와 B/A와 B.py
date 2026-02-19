import sys
input = sys.stdin.readline

def isSame(S, T):
    for i in range(s_len):
        if(S[i]!=T[i]):
            return 0
    return 1

def process(T):
    while s_len<len(T):
        last = T.pop()
    
        if (last=='B'):
            T.reverse()

S = list(input().rstrip())
T = list(input().rstrip())
s_len = len(S)

process(T)
print(isSame(S,T))
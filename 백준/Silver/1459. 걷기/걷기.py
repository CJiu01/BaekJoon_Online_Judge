import sys

def solve(X, Y, W, S):
    ans = 0
    if 2*W <= S:
        ans = (X+Y) * W
    elif W<S<2*W:
        ans = min(X,Y)*S + abs(X-Y)*W
    else:
        if (X+Y)%2 == 0:
            ans = max(X,Y)*S
        else:
            ans = (max(X,Y)-1)*S + W
    return ans
    
def main():
    X, Y, W, S = map(int, input().split())
    answer = solve(X, Y, W, S)
    print(answer)

if __name__ == "__main__":
    main()
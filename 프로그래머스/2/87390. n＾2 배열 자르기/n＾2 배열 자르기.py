def solution(n, left, right):
    b = []
    for k in range(left, right+1):
        row, col = k//n, k%n
        b.append(max(row, col)+1)
    return b
from itertools import permutations

def solution(n, k):
    return list(permutations(range(1,n+1),n))[k-1]

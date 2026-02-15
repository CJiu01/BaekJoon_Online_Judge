import sys
input = sys.stdin.readline
from itertools import combinations

l, c = map(int, input().split())
al = list(input().split())
list.sort(al)
vowel = {'a', 'e', 'i', 'o', 'u'}

for password in combinations(al, l):
    cnt = len(set(password) & vowel)
    if (0<cnt and cnt<=l-2):
        print(''.join(password))
import sys
input = sys.stdin.readline

def isValid(list):
    # 0<vo<=l-2
    vowel = {'a', 'e', 'i', 'o', 'u'}
    cnt = len(set(list) & vowel)
    if (0<cnt and cnt<=l-2):
        return True
    else:
        return False

def dfs(arr, cur):
    if(len(arr)==l):
        if (isValid(arr)):
            print(''.join(arr))
        return

    for i in range(cur,c):
        dfs(arr+[al[i]], i+1)

l, c = map(int, input().split())
al = list(input().split())
list.sort(al)

dfs([], 0)
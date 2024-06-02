import sys
input = sys.stdin.readline

s = input().strip()
stack = []
ig = False
for i in range(len(s)):

    if ig == False: 
        if s[i] == ' ' or s[i] == '<':
            if stack:
                print(''.join(stack[::-1]), end='')
                stack = []

            if s[i] == '<':
                ig = True
            else:
                print(' ',end='')
                continue
        else:
            stack.append(s[i])
            continue     
    stack.append(s[i])

    if s[i] == '>':
        ig = False
        print(''.join(stack), end='')
        stack = []

if s[0] != ' ':
    print(''.join(stack[::-1]))

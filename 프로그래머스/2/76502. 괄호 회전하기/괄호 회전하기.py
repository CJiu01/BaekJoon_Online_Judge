def check(s):
    left = {'(':0, '[':1, '{':2}
    right = {')':0, ']':1, '}':2}
    stack = []
    for i in s:
        if i in left.keys():
            stack.append(left[i])
        else:
            if not stack or stack[-1] != right[i]: 
                return 0
            stack.pop()
    if not stack:
        return 1
    return 0

def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
        rotated = s[i:n]+s[:i]
        if check(rotated):
            answer += 1
    
    return answer
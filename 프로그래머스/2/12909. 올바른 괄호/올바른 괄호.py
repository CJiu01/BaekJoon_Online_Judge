def solution(s):
    s = list(s)
    stack = []

    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    
    if len(stack) > 0:
        return False
    else:
        return True

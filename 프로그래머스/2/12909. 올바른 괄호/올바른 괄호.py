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
    
    return not stack
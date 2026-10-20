def correct(p):
    stack = []
    for i in range(len(p)):
        if p[i]==')':
            if not stack:
                return False
            else:
                stack.pop()
        else:
            stack.append(1)
    if stack:
        return False
    return True

def sep(p):
    i=1
    s = 1 if p[0]=='(' else -1
    while i<len(p) and s:
        if s == 0:
            break
        if p[i]=='(':
            s += 1
        else:
            s -= 1
        i+=1
    u,v= p[:i],p[i:]
    
    return (u,v)

def s(p):
    p = p[1:-1]
    t = ''
    for i in range(len(p)):
        if p[i]=='(':
            t += ')'
        else:
            t += '('
    return t
        
def r(p):
    global answer
    if not p:
        return '' 
    u, v = sep(p)
    if correct(u):
        return u +r(v)
    else:
        return '('+r(v)+')'+s(u)
    
def solution(p):    
    return r(p) 
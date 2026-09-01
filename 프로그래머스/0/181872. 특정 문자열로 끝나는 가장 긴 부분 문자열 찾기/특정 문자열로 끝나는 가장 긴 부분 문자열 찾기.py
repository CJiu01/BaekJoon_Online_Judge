def solution(myString, pat):
    answer = ''
    for i in range(len(myString)):
        if myString[i:].startswith(pat):
            answer = i
    
    return myString[:answer]+pat
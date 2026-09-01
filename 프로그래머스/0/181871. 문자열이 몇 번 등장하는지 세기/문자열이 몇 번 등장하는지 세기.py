def solution(myString, pat):
    answer = 0
    l = len(pat)
    for i in range(len(myString)-l+1):
        if myString[i:i+l] == pat:
            answer+=1
    
    return answer
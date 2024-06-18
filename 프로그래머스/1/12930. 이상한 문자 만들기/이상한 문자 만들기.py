def solution(s):
    answer = ''

    d = True
    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
            d = True
        else:
            if d:
                answer += s[i].upper()
            else:
                answer += s[i].lower()
            d = not d

    return answer
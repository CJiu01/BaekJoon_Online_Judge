def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    
    for p in photo:
        score = 0
        for person in p:
            if person in name:
                score += dic[person]
        answer.append(score)
    return answer

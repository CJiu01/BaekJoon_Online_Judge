from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    case = [i for i in range(0,len(dungeons))]
    case = list(permutations(case, len(dungeons)))

    for i in case:
        cnt = 0
        current_heal = k
        for j in i:
            if dungeons[j][0] > current_heal:
                break
            current_heal -= dungeons[j][1]
            cnt += 1

        if cnt > answer:
            answer = cnt
    
    return answer
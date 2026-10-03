def solution(sequence, k):
    answer = []
    
    cur = 0
    i, j = 0,0
        
    while j<=len(sequence):
        if cur==k:
            answer.append([j-i,i,j-1])
            cur -= sequence[i]
            i+=1
        elif cur>k:
            cur -= sequence[i]
            i+=1
        else:
            if j==len(sequence):
                break
            cur += sequence[j]
            j+=1
    
    answer.sort()
    return [answer[0][1], answer[0][2]]
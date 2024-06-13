def solution(genres, plays):
    answer = []
    
    dic = {}

    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]].append([plays[i],i])
        else:
            dic[genres[i]] = [[plays[i],i]]
    
    
    arr = []
    for i in dic:
        arr.append(dic[i])
    

    for i in range(len(arr)):
        arr[i].sort(key=lambda x: (-x[0],x[1]))


    
    count = [0]*len(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            count[i] += arr[i][j][0]


    
    
    for i in range(len(count)):
        m = count.index(max(count))
        
        for j in range(2):
            try:
                answer.append(arr[m][j][1])
            except IndexError:
                break
        count.pop(m)
        arr.pop(m)
    
    return answer
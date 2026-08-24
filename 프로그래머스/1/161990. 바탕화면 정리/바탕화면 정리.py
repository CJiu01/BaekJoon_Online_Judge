def solution(wallpaper):
    answer = [100,100,-1,-1]
    width = len(wallpaper[0])
    length = len(wallpaper)
    
    for i in range(length):
        for j in range(width):
            if wallpaper[i][j] == "#":
                if i<answer[0]:
                    answer[0] = i
                if j<answer[1]:
                    answer[1] = j
                if i>=answer[2]:
                    answer[2] = i+1
                if j>=answer[3]:
                    answer[3] = j+1
    return answer
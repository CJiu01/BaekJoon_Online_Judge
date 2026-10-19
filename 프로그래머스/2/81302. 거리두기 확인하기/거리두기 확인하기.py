def check_distance(place, x,y):
    
    st = [[-1,0],[0,-1],[1,0],[0,1]]
    cross = [[-1,-1],[-1,1],[1,-1],[1,1]]
    
    for i in range(4):
        for t in range(1,3):
            dx = x+(st[i][0]*t)
            dy = y+(st[i][1]*t)
            if 0<=dx<5 and 0<=dy<5:
                if place[dx][dy] == 'X':
                    break
                elif place[dx][dy] == 'P':
                    return 0
    
    for i in range(4):
        dx = x+cross[i][0]
        dy = y+cross[i][1]
        if 0<=dx<5 and 0<=dy<5:
            if place[dx][dy] == 'O' or place[dx][dy] == 'X':
                continue
            if place[x][dy] == 'X' and place[dx][y] == 'X':
                continue
            return 0
    return 1


def solution(places):
    answer = []
    
    for place in places:
        res = 1
        
        for i in range(5): 
            for j in range(5):
                if place[i][j] == 'P':
                    res = check_distance(place, i,j)
                    if not res:
                        answer.append(res)
                        break
            if not res:
                break
        if res:
            answer.append(1)
    
    return answer
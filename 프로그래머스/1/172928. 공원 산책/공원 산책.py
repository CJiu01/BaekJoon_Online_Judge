def find_position(park, length, width):
    # 현재 위치 찾기
    position = []
    for i in range(length):
        if "S" in park[i]:
            for j in range(width):
                if park[i][j] == "S":
                    position = [i,j]
                    return position


def solution(park, routes):
    answer = []
    position = []
    width = len(park[0])
    length = len(park)
    dic = {'E': [0,1], 'W':[0,-1], 'S':[1,0], 'N':[-1,0]}

    position = find_position(park, length, width)
    
    for route in routes:
        dir,size = route.split(' ')
        size = int(size)
        flag = True
        
        tmp_x, tmp_y = position[0], position[1]
        for i in range(size):    
            tmp_x += dic[dir][0]
            tmp_y += dic[dir][1]
            if (0>tmp_x or tmp_x>=length or 0>tmp_y or tmp_y>=width) or park[tmp_x][tmp_y] == "X":
                flag = False
                break
        
        if flag:
            position = [tmp_x, tmp_y]

    return position
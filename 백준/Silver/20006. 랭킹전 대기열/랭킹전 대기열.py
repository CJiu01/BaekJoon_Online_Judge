import sys
input = sys.stdin.readline

def solution(p,m):
    room_info = []
    room = [[] for i in range(p)]
    
    for i in player:
        j = 0
        while True:
            try:
                if (room_info[j][0]-10) <= int(i[0]) <= (room_info[j][0]+10):
                    if room_info[j][1] < m:
                        room_info[j][1] += 1
                        room[j].append(i)
                        break
                j += 1
            except IndexError:
                room_info.append([int(i[0]),1])
                room[j].append(i)
                break  
    for i in room:
        i.sort(key= lambda x: x[1])

    for i in range(len(room_info)):
        if room_info[i][1] < m:
            print("Waiting!")
            for j in range(len(room[i])):
                print(room[i][j][0], room[i][j][1])
        else:
            print("Started!")
            for j in range(len(room[i])):
                print(room[i][j][0], room[i][j][1])

p, m = map(int,input().split())
player = []
for i in range(p):
    player.append(list(input().split()))

solution(p,m)
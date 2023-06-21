x, y, w, h = map(int, input().split(' '))
shortest_distance = []
shortest_distance.append(x)
shortest_distance.append(y)
shortest_distance.append(w-x)
shortest_distance.append(h-y)
    
print(min(shortest_distance))
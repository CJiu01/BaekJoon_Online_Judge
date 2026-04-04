dish = input()
sum = 10
for i in range(1,len(dish)):
    if dish[i-1] == dish[i]:
        sum += 5
    else:
        sum += 10

print(sum)
x = []
for i in range(5):
    x.append(int(input()))
print(int(sum(x) / 5))
x.sort()
print(x[2])
n = 1000 - int(input())
count = 0

array = [500, 100, 50, 10, 5, 1]
for coin in array:
    count += (n//coin)
    n %= coin
    
print(count)
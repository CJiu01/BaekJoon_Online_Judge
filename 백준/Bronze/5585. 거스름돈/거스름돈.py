money = [500, 100, 50, 10, 5, 1]

user = int(input())
user_change = 1000-user
count = 0

for i in money:
    count += user_change//i
    user_change %= i
    
        
print(count)
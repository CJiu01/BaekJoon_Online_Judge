n = int(input())

end = 666 
count = 0
while True: 
    if '666' in str(end): 
        count += 1 
        if count == n: 
            break 
    end += 1
print(end)

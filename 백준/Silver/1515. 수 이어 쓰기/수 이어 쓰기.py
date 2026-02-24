s = input()
i=1
while s:
    i_str = str(i)

    for t in i_str:
        if(s and t==s[0]):
            s=s[1:]
    i+=1
    
print(i-1)
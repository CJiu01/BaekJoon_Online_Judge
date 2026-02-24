s = input()
idx = 0
n = 0

while (idx < len(s)):
    n+=1
    
    for digit in str(n):
        if (digit == s[idx]):
            idx+=1
            
            if (idx == len(s)):
                break
            
print(n)
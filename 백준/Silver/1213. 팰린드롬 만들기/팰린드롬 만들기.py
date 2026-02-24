from collections import Counter

def palindrome():
    odd = 0
    ans = ''

    for value in name.values():
        if(value%2==1):
            odd+=1
            
    if (odd>1):
        ans = "I'm Sorry Hansoo"
        return ans

    al = [chr(i+65) for i in range(26)]      
    for i in al:
        if(i in name):
            ans += i*(name[i]//2)
            name[i] %= 2
            if(name[i]==0):
                del name[i]
            else:
                odd = i
                
    suffix = ans[::-1]
    if name:
        ans += odd
    ans += suffix
    return ans
            

name = Counter(input())
print(palindrome())

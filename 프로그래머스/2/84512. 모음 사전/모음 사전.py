def solution(word):
    answer = 0
    vowels = ['A','E','I','O','U']
    cur = []
    
    def dfs():
        nonlocal answer 

        if ''.join(cur) == word:
            return True
        elif len(cur) == 5:
            return False
        
        for vowel in vowels:
            cur.append(vowel)
            answer += 1
  
            if dfs():
                return True
            cur.pop()
            
        return False
    
    dfs()
    return answer
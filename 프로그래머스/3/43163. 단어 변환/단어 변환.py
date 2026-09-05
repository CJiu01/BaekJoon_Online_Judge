from collections import deque

def count_diff(a,b):
    cnt = 0 
    for i in range(len(a)):
        if a[i]==b[i]:
            continue
        cnt+=1
    if cnt==1:
        return True
    return False


from collections import deque

def bfs(begin, target, visited, words, n):
    cnt = 0
    q = deque([begin])
    tmp = [1]
    while tmp:
        tmp = deque()
        while q:
            cur_word = q.popleft()
            if cur_word == target:
                return cnt 
            
            for i in range(n):
                if not visited[i]:
                    if count_diff(cur_word, words[i]):
                        visited[i] = True
                        tmp.append(words[i])
        if tmp:
            q = tmp
            cnt += 1
        else:
            return -1
                
    return -1
    

def solution(begin, target, words):    
    n = len(words)
    visited = [False] * n
    
    if not target in words:
        return 0
    answer = bfs(begin, target, visited, words, n)
    
    return answer if answer!=-1 else 0
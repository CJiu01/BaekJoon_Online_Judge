def print_brace(words,p,q):
    word = words[p]
    res = word[:q]+'['+word[q]+']'+word[q+1:]
    words[p] = res
    print(' '.join(words))
    
N = int(input()) 
keys = [False]*26

for _ in range(N):

    words = list(input().split())
    flag = False
    for i in range(len(words)):
        low = ord(words[i][0].lower())-97
        if not keys[low]:
            keys[low] = True
            print_brace(words,i,0)
            flag = True
            break
    if flag:
        continue
            
    flag = False
    for i in range(len(words)):
        for j in range(1,len(words[i])):
            low = ord(words[i][j].lower())-97
            if not keys[low]:
                keys[low] = True
                print_brace(words,i,j)
                flag = True
                break
        if flag:
            break
    if not flag:
        print(' '.join(words))

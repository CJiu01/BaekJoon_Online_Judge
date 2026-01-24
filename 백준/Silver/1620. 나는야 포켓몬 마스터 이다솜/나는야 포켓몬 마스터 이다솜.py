n,m = map(int, input().split())

dic = {}
for i in range(1,n+1):
    pocket = input()
    dic[pocket] = i
    
name_keys = list(dic.keys())

for _ in range(m):
    user = input()
    if(user.isdigit()):
        idx = int(user)-1
        print(name_keys[idx])
    else:
        print(dic.get(user))

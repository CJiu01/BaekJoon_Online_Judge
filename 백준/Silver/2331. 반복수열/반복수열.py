A, P = input().split()
P = int(P)


res = 0
D =[]
while not (res in D):
    D.append(A)
    
    res = 0
    for i in A:
        res += int(i)**P

    res=A=str(res)

for i in range(len(D)):
    if res == D[i]:
        break
print(i)
a = input()
b = input()

answer = ''
for c in b:
    if not c in a:
        answer += c
print(answer)
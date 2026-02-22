import sys
input = sys.stdin.readline

N, game = input().split()
people = set()

for _ in range(int(N)):
    name = input().rstrip()
    people.add(name)
    
res = 0
length = len(people)
if game=='Y':
    res = length
elif game =='F':
    res = length//2
elif game == 'O':
    res = length//3
print(res)
sentence = []
vowel= ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']

player = input()

while(player != '#'):
    sentence.append(player)
    player = input()

for i in sentence:
    vowel_count = 0
    for j in i:
        if j in vowel:
            vowel_count += 1
    
    print(vowel_count)
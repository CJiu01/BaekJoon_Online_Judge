from itertools import combinations

L, C = map(int, input().split())
letters = sorted(input().split())

vowels = 'aeiou'
for comb in combinations(letters, L):
    vowel_count = sum(1 for c in comb if c in vowels)
    if (vowel_count>0 and vowel_count<=L-2):
        print(''.join(comb))
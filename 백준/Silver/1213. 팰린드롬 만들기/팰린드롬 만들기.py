word = input()
word_dic = {}

for w in word:
    word_dic[w] = word_dic.get(w,0)+1 
    
odd_count = 0
sorted_keys = sorted(word_dic.keys())

prefix = ''
mid = ''

for k in sorted_keys:
    if (word_dic[k]%2==1):
        mid += k
        odd_count += 1
    prefix += k*(word_dic[k]//2)
    
suffix = prefix[::-1]

if odd_count>1:
    print("I'm Sorry Hansoo")
else:
    print(prefix+mid+suffix)
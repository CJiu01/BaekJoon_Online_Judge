star_rows = int(input())

for i in range(1,star_rows+1):
    j = star_rows-i
    print(' '*j,end='')
    print('*'*i)
    j -= 1

// 수정
star_rows = int(input())

for i in range(1,star_rows+1):
    print(' '*(star_rows-i)+'*'*i)

def solution(arr):
    answer = [0,0]
    
    def check(size, x,y):
        if size == 1:
            answer[arr[x][y]] += 1
            return
        
        else:
            first = arr[x][y]
            
            for dx in range(size):
                for dy in range(size):
                    if first != arr[x + dx][y + dy]:
                        check(size//2, x,y)
                        check(size//2, x+size//2,y)
                        check(size//2, x,y+size//2)
                        check(size//2, x+size//2,y+size//2)
                        return
            answer[first] += 1
        
    check(len(arr),0,0)
    return answer
import Foundation

// 1343

func solution() {
    var input = Array(readLine()!)
    var i = 0
    var cnt = 0
    
    while i<input.count {

        if input[i] == "X" {
            cnt += 1
        }
        
        if cnt == 2 && ( i+1 == input.count || input[i+1] != "X") {
            input[i] = "B"
            input[i-1] = "B"
            cnt = 0
        } else if cnt == 4 {
            input[i] = "A"
            input[i-1] = "A"
            input[i-2] = "A"
            input[i-3] = "A"
            cnt = 0
        } else if input[i] == "." || i+1 == input.count {
            if cnt % 2 == 1 {
                print("-1")
                break
            }
        }
    
        i += 1
    }
    
    if i == input.count {
        for n in input {
            print(n, terminator: "")
        }
        print()
    }
}

solution()
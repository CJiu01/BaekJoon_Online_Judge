func solution() {
    let input = Int(readLine()!)!
    var i = 0
    var blank = input-1
    var direction = true
    
    for n in 0..<(input*2-1) {
        print(String(repeating: " ", count: blank),terminator: "")
        print(String(repeating: "*", count: (2*i+1)),terminator: "")
        print()
        
        if n == input-1 {
            direction.toggle()
        }
        
        if direction {
            i += 1
            blank -= 1
        } else {
            i -= 1
            blank += 1
        }
    }
    print()
}

solution()
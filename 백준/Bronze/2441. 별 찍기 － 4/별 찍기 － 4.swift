func solution() {
    var n = Int(readLine()!)!
    for i in 0..<n {
        var res = ""
        for _ in 0..<i {
            print(" ", terminator: "")
        }
        for _ in 0..<n-i {
            print("*", terminator: "")
        }
        print()
    }
}

solution()

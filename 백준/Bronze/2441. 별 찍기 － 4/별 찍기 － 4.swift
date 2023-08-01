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


// Refactor

let n = Int(readLine()!)!

for i in 0..<n {
    print(String(repeating: "", count: i) + String(repeating: "*", count: n-i))
}

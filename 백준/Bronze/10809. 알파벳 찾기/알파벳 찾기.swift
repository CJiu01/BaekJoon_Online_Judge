let s = readLine()!

for i in 97..<123 {
    let al = Character(UnicodeScalar(i)!)
    if let index = s.firstIndex(of: al) {
        print(s.distance(from: s.startIndex, to: index), terminator: " ")
    } else {
        print(-1, terminator: " ")
    }
}
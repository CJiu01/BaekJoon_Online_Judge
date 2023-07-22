func solution() {
    let input = Int(readLine()!)!
    let base = readLine()!
    var result: [Character] = Array(base)
    
    for i in 0..<input-1 {
        let sentence = readLine()!
        for j in 0..<base.count {
            if base[base.index(base.startIndex, offsetBy: j)] != sentence[sentence.index(sentence.startIndex, offsetBy: j)] {
                result[j] = "?"
            }
        }
    }
    result.forEach { print($0, terminator: "")}
}

solution()
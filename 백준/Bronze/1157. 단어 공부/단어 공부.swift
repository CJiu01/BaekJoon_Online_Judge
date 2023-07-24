func solution()-> String {
    var input = readLine()!
    input = input.lowercased()
    var inputCount = Array(repeatElement(-1, count: 26))
    
    input.forEach { inputCount[Int(($0).asciiValue!)-97] += 2 }
    var maxIndex = 0
    var maxElement = 0
    
    for i in 0..<inputCount.count {
        if inputCount[i] == maxElement {
            if inputCount[i] == inputCount.max() {
                return "?"
            }
        } else if inputCount[i] > maxElement {
            maxIndex = i
            maxElement = inputCount[i]
        }
    }
    return String(Unicode.Scalar(maxIndex+65)!)
}

print(solution())
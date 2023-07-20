func solution() {
    var input = readLine()!.split(separator: " ").map { Int($0)! }
    input = input.sorted()
    input.forEach { print($0, terminator: " ")}
}

solution()
func solution() {
    let input = readLine()!
    let reversedInput = String(input.reversed())
    let result: String = input == reversedInput ? "1" : "0"
    print(result)
}

solution()
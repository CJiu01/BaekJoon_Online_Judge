while true {
    if let input = readLine() {
        print(input)
    } else {
        break
    }
}

// Refactor
while let input = readLine() {
    print(input)
}

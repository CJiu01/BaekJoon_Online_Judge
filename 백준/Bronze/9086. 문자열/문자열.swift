for i in 0..<Int(readLine()!)! {
    let input = readLine()!
    print(input[input.startIndex], input[input.index(before: input.endIndex)], separator: "")
}
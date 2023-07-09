func symbolCalculator(A: Int, B: Int) -> Int {
    
    let answer = (A+B)*(A-B)
    return answer
    
}

let input = readLine()!.split(separator: " ").map { Int($0)! }
print(symbolCalculator(A: input[0], B: input[1]))

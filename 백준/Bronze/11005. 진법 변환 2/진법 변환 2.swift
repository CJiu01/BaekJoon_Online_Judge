let input = readLine()!.split(separator: " ").map{ Int($0)! }
let result = String(input[0], radix: input[1])
print(result.uppercased())
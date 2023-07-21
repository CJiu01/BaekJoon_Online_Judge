func solution() {
    var personA = readLine()!.split(separator: " ").map { Int($0)! }.reduce(0, +)
    var personB = readLine()!.split(separator: " ").map { Int($0)! }.reduce(0, +)
    print(personA > personB ? personA : personB)
}
solution()
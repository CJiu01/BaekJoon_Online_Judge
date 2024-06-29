let t = Int(readLine()!)!
for _ in 0..<t {
    let input = readLine()!.split(separator: " ")
    var res = ""
    for i in input[1] {
        res += String(Array(repeating: i, count: Int(input[0])!))
    }
    print(res)
}
let input = readLine()!
var result: String = ""
input.map {
    if ($0.asciiValue ?? 0 > 64) && ($0.asciiValue ?? 0 < 94) {
        result += $0.lowercased()
    } else {
        result += $0.uppercased()
    }
}
print(result)
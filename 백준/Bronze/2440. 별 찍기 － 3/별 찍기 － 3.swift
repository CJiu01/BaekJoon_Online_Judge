import Foundation

let n = Int(readLine()!)!

for i in 0..<n {
    var res = ""
    for _ in stride(from: n, to: i, by: -1) {
        res += "*"
    }
    print(res)
}
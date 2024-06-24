var arr = Array(1...30)

for _ in 0..<28 {
    let i = arr.firstIndex(of: Int(readLine()!)!)!
    arr.remove(at: i)
}
arr.forEach { print($0) }
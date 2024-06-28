let t = Int(readLine()!)!
for _ in 0..<t {
    let s = readLine()!
    print(s[String.Index(encodedOffset:0)],s[String.Index(encodedOffset: s.count-1)],separator: "")
}
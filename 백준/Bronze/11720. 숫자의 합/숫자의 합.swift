let n = Int(readLine()!)!
let s = readLine()!
var res = 0
for i in 0..<n {
    res += Int(String(s[String.Index(encodedOffset: i)]))!
}

print(res)
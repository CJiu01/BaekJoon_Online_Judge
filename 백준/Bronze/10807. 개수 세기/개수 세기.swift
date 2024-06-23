let n = Int(readLine()!)!
let arr = readLine()!.split(separator: " ").map { Int($0)! }
let target = Int(readLine()!)!

var cnt = 0
for i in arr {
    if i==target {
        cnt += 1
    }
}

print(cnt)
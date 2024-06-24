var user = Set<Int>()
for _ in 0..<10 {
    let num = Int(readLine()!)!
    user.insert(num%42)
}

print(user.count)
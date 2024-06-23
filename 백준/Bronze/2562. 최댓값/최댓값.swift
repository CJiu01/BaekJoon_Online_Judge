var arr = [Int]()
for i in 0..<9 {
    arr.append(Int(readLine()!)!)
}

let maxValue = arr.max()!
print(maxValue)
print(arr.firstIndex(of: maxValue)!+1)
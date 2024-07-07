import Foundation

var arr = [[Int]]()

for i in 0..<9 {
    arr.append(Array(readLine()!.split(separator: " ").map { Int($0)! }))
}

var tmp: [[Int]] = []
var maxValue = 0
var (a,b) = (0,0)
for i in 0..<9 {
    let tmpValue = arr[i].max()!
    if tmpValue >= maxValue {
        a = i+1
        b = arr[i].firstIndex(of: tmpValue)!+1
        maxValue = tmpValue
    }
}
print(maxValue)
print(a, b)
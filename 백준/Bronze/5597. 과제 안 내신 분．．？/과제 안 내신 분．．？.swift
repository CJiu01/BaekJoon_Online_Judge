import Foundation

// 5597

// Set 생성 및 선언
var integerSet: Set<Int> = Set<Int>()
var userSet: Set<Int> = Set<Int>()

for i in 1..<31 {
    integerSet.insert(i)
}

for i in 0..<28 {
    userSet.insert(Int(readLine()!)!)
}
let subSet: Set<Int> = integerSet.subtracting(userSet)
for i in subSet.reversed() {
    print(i)
}
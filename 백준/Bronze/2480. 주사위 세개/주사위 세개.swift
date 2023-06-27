import Foundation

let array = readLine()!.components(separatedBy: " ").map { Int($0)! }
var sameNumberCount = 0
var sameNumber = 0
var maxNumber = 0
for i in 0..<3 {
    for j in (i+1)..<3 {
        if array[i] == array[j] {
            sameNumberCount += 1
            sameNumber = array[i]
        }
    }
    if maxNumber < array[i] {
        maxNumber = array[i]
    }
}

if sameNumberCount == 0 {
    print(maxNumber*100)
} else if sameNumberCount == 3 {
    print(10000+sameNumber*1000)
} else {
    print(1000+sameNumber*100)
}

// 입력받기 수정 -> (정렬까지 한 번에)
// var array = readLine()!.split(separator: " ").map { Int($0)! }.sorted()

import Foundation

let partyPlace = readLine()!.split(separator: " ").map { Int($0)! }
let expectedNumber = partyPlace[0]*partyPlace[1]

let articleNumber = readLine()!.split(separator: " ").map { Int($0)! }
for i in 0..<5 {
    print(articleNumber[i]-expectedNumber, terminator: " ")
}

// Refactor
let partyPlace: Int = {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    return input[0]*input[1]
}()
print(readLine()!.split(separator: " ").map { String(Int($0)! - partyPlace) }.joined(separator: " "))

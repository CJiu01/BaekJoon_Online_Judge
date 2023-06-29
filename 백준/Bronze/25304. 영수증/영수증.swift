import Foundation

let expectedTotalPrice = Int(readLine()!)!
var computedTotalPrice = 0

for i in 0..<Int(readLine()!)! {
    
    var array = readLine()!.split(separator: " ").map { Int($0)! }
    computedTotalPrice += (array[0]*array[1])
}

if(computedTotalPrice == expectedTotalPrice) {
    print("Yes")
} else {
    print("No")
}
import Foundation

var hamburger = Array<Int>()
var drink = Array<Int>()

for _ in 0..<3 {
    hamburger.append(Int(readLine()!)!)
}
for _ in 0..<2 {
    drink.append(Int(readLine()!)!)
}

print(hamburger.min()! + drink.min()! - 50)

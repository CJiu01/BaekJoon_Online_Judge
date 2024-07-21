import Foundation

var n = Int(readLine()!)!
var cnt = 1

for i in 0..<n {
    cnt *= 2
}
print((cnt+1)*(cnt+1))
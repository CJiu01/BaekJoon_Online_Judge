import Foundation

let input1 = Int(readLine()!)!
let input2 = readLine()!.map { Int(String($0))! }
var res = 0
for i in 0..<3 {
    var tmp = input1*input2[2-i]
    print(tmp)
    res += tmp*Int(pow(10, Double(i)))
}
print(res)
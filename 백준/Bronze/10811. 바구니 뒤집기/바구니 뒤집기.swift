let input = readLine()!.split(separator: " ").map { Int($0)! }
let (N,M) = (input[0],input[1])
var basket = Array(0...N)

for _ in 0..<M {
    let num = readLine()!.split(separator: " ").map { Int($0)! }
    var tmp = basket
    for i in 0..<num[1]-num[0]+1 {
        tmp[num[0]+i] = basket[num[1]-i]
    }
    basket = tmp
}
print(basket[1...].map{String($0)}.joined(separator: " "))
let input = readLine()!.split(separator: " ").map { Int($0)! }
let (N,M) = (input[0],input[1])

var basket = Array(repeating:0, count: N)
var ball = [[Int]]()
for _ in 0..<M {
    ball.append(readLine()!.split(separator: " ").map { Int($0)! })
}

for i in ball {
    for j in i[0]...i[1] {
        basket[j-1] = i[2]
    }
}
print(basket.map { String($0) }.joined(separator: " "))
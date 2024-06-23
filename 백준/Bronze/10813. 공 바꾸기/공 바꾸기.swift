let input = readLine()!.split(separator: " ").map { Int($0)! }
let (N,M) = (input[0],input[1])

var basket = Array<Int>(0...N)


for i in 0..<M {
    let ball = readLine()!.split(separator: " ").map { Int($0)! }
    let tmp = basket[ball[0]]
    basket[ball[0]] = basket[ball[1]]
    basket[ball[1]] = tmp
}

print(basket[1...].map { String($0) }.joined(separator: " "))
let input = readLine()!.split(separator: " ").map{ Int($0)! }
let arr = readLine()!.split(separator: " ").map { Int($0)! }
let (N,X) = (input[0],input[1])

for i in arr {
    if i<X {
        print(i, terminator: " ")
    }
}
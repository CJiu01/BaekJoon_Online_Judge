import Foundation

let score: [Int: String] = [0: "E", 1: "A", 2: "B", 3: "C", 4: "D"]

for _ in 0..<3 {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    var cnt = 0
    for i in 0..<4 {
        if input[i] == 0 {
            cnt += 1
        }
    }
    print(score[cnt]!)
}

// 고차함수 reduce를 통한 refactor
for _ in 0..<3 {
    let input = readLine()!.split(separator: " ").map { Int($0)! }.reduce(0, +)
    print(input>3 ? "E" : input>2 ? "A" : input>1 ? "B" : input>0 ? "C" : "D")
}

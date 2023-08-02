import Foundation

func solution() {
    let n = Int(readLine()!)!
    var cnt = 1
    for i in 0..<n {
        print(String(repeating: " ", count: i)+String(repeating: "*", count: 2*n-cnt))
        cnt += 2
    }
}

solution()

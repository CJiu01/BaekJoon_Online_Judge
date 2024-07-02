func solution(_ n:Int) -> Int {
    var check = Array(repeating: 0, count: n + 1)
    var cnt = 0

    for i in 2...n {
        if check[i] == 0 {
            cnt += 1
            
            for j in stride(from: i, to: n + 1, by: i) {
                check[j] = 1
            }
        }
    }

    return cnt
}

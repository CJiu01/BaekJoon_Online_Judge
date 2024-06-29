import Foundation

func solution(_ progresses: [Int], _ speeds: [Int]) -> [Int] {
    var numOfReleases: [Int] = []
    var left: [Int] = []
    
    for i in 0..<progresses.count {
        left.append(Int(ceil(Double(100-progresses[i])/Double(speeds[i]))))
    }
    
    while !left.isEmpty {
        var cnt = 1
        var lastReleaseDate = left.removeFirst()
        while true {
            if lastReleaseDate >= left.first ?? 101 {
                left.removeFirst()
                cnt += 1
            } else {
                break
            }
        }
        numOfReleases.append(cnt)
    }
    return numOfReleases
}
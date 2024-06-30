import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
    
    var queue: [[Int]] = []
    for i in 0..<priorities.count {
        queue.append([priorities[i],i])
    }
    
    var cnt = 0
    while !queue.isEmpty {
        let firstElement = queue.map { $0[0] }
        let maxValue = firstElement.max()

        if queue[0][0] == maxValue {
            cnt += 1
            if queue[0][1] == location {
                return cnt
            }
            queue.removeFirst()
        } else {
            queue.append(queue.removeFirst())
        }
    }
    return 100
}
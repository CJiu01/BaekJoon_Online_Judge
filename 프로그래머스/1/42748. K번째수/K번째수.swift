import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var res: [Int] = []
    for command in commands {
        var target = array
        var sliceArr = Array(target[command[0]-1..<command[1]])
        sliceArr.sort()
        res.append(sliceArr[command[2]-1])
    }
    return res
}
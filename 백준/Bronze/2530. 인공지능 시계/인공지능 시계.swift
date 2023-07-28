import Foundation

func solution() {

    let currentTime = readLine()!.split(separator: " ").map{ Int($0)! }
    var (hour, minute, second) = (currentTime[0], currentTime[1], currentTime[2])

    let cookingTime = Int(readLine()!)!
    var totalSeconds = hour * 3600 + minute * 60 + second + cookingTime

    second = totalSeconds % 60
    totalSeconds /= 60

    minute = totalSeconds % 60
    totalSeconds /= 60

    hour = totalSeconds % 24

    print("\(hour) \(minute) \(second)")

}
solution()
import Foundation

func solution() {
    var input = readLine()!
    
    while input != "# 0 0" {
        var array = input.split(separator: " ")
        if (Int(array[1])! > 17) || (Int(array[2])! >= 80) {
            print(array[0], "Senior")
        } else {
            print(array[0], "Junior")
        }
        input = readLine()!
    }
}

solution()
import Foundation

func solution() {
    let input = readLine()!.map { Int(String($0))! } 
    let sortedInput = input.sorted(by: >)
    
    sortedInput.forEach { print($0, terminator: "") }
    print()
}

solution()

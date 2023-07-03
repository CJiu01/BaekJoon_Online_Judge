import Foundation

func factor(_ a: Int, _ b: Int) -> Bool {
    if a<b {
        if b%a == 0 {
            return true
        }
    }
    return false
}

func multiple(_ a: Int, _ b: Int) -> Bool {
    if a>b {
        if a%b == 0 {
            return true
        }
    }
    return false
}

while true {
    
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    if input[0]==0, input[1]==0 {
        break
    }
    
    if factor(input[0],input[1]) {
        print("factor")
    } else if multiple(input[0],input[1]) {
        print("multiple")
    } else {
        print("neither")
    }
    
}

// Refactor

while true{
    let ab = readLine()!.split(separator: " ").map { Int($0)! }
    if ab == [0, 0] {
        break
    }
    let a=ab[0]
    let b=ab[1]
    if b%a == 0 {
        print("factor")
    } else if a%b == 0 {
        print("multiple")
    } else {
        print("neither")
    }
    
}

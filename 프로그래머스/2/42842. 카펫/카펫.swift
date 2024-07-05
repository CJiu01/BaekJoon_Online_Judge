import Foundation

func solution(_ brown:Int, _ yellow:Int) -> [Int] {
    
    for i in 1...Int(sqrt(Double(yellow))) {
        if yellow%i == 0 {
            if ((i+2)+(yellow/i))*2 == brown {
                return [yellow/i+2, i+2]
            }
        }
    }
    return []
}
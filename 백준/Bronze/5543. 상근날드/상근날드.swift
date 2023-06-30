import Foundation

class Beakjoon5543 {
    
    var hamburger = Array<Int>()
    var drink = Array<Int>()
    
    func getData() {
        for i in 1 ... 5 {
            let input = readLine()!
            
            if i < 4 {
                hamburger.append(Int(input)!)
            }
            else {
                drink.append(Int(input)!)
            }
        }
        solution()
    }
    
    func solution() {

        hamburger.sort()
        drink.sort()
        let res = hamburger[0] + drink[0] - 50
        print(res)
    }
}

let beakjoon = Beakjoon5543()
beakjoon.getData()
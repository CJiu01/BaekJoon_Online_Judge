import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    var sizes = sizes
    for i in 0..<sizes.count {
        sizes[i].sort(by: >)
    }
    var a = 0
    var b = 0
    for i in 0..<sizes.count {
        if sizes[i][0]>a {
            a = sizes[i][0]
        }
        if sizes[i][1]>b {
            b = sizes[i][1]
        }
    }    
    return a*b
}
import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var dic = [String: Int]()
    
    for i in clothes {
        if let type = dic[i[1]] {
            dic[i[1]]? += 1
        } else {
            dic[i[1]] = 1
        }
    }
    
    var res = 1
    dic.forEach { res *= ($0.value+1) }
    return res>0 ? res-1 :  0
}
import Foundation

func solution(_ genres:[String], _ plays: [Int]) -> [Int] {
    var dic = [String: [[Int]]]()
    var cnt = [String: Int]()
    
    for i in 0..<genres.count {
        if let genre = dic[genres[i]] {
            dic[genres[i]]?.append([i,plays[i]])
            cnt[genres[i]]? += plays[i]
        } else {
            dic[genres[i]] = [[i,plays[i]]]
            cnt[genres[i]] = plays[i]
        }
    }
    
    for key in dic.keys {
        dic[key]?.sort(by: { $0[1] > $1[1] })
    }
    let ord = Array(cnt.sorted(by: { $0.value > $1.value }))
    print(ord)
    
    var res = [Int]()
    for genre in ord {
        print(genre)
        for i in 0..<2 {
            if i >= dic[genre.key]?.count ?? 0 { break }
            res.append(dic[genre.key]?[i][0] ?? -1)
            
        }
    }
    return res
}
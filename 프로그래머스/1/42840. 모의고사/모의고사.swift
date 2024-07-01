import Foundation

func solution(_ answers:[Int]) -> [Int] {
    let student1 = [1,2,3,4,5]
    let student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    let student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    var ans1 = 0
    var ans2 = 0
    var ans3 = 0
    
    for i in 0..<answers.count {
        if answers[i]==student1[i%5] {
            ans1 += 1
        }
        if answers[i]==student2[i%8] {
            ans2 += 1
        }
        if answers[i]==student3[i%10] {
            ans3 += 1
        }
    }
    
    var res: [Int] = []
    let maxNum = max(ans1, ans2, ans3)
    if maxNum == ans1 {
        res.append(1)
    }
    if maxNum == ans2 {
        res.append(2)
    }
    if maxNum == ans3 {
        res.append(3)
    }
    return res
}
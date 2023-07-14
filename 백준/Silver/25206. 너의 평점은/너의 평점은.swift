import Foundation

func solution() {
    let courseCreditDictionary: [String: Float] = ["A+": 4.5,
                                                   "A0": 4.0,
                                                   "B+": 3.5,
                                                   "B0": 3.0,
                                                   "C+": 2.5,
                                                   "C0": 2.0,
                                                   "D+": 1.5,
                                                   "D0": 1.0,
                                                   "F": 0.0]
    var sum = 0.0
    var grade = 0.0
    for _ in 0..<20 {
        let subject = readLine()!.split(separator: " ")
        if subject[2] != "P" {
            grade += Double(subject[1])!
            sum = sum + Double((Float(subject[1])! * (courseCreditDictionary[String(subject[2])] ?? 0.0)))
        }
    }
    print(sum/grade)
}

solution()
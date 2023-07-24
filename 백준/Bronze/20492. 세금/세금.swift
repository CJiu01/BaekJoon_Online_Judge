import Foundation

func solution() {
    let input = Int(readLine()!)!
    let prizeMoney = calculatePrizeMoney(prize: input)
    print("\(prizeMoney.case1) \(prizeMoney.case2)")

}

solution()


func calculatePrizeMoney(prize: Int) -> (case1: Int, case2: Int) {
    let taxRate = 0.22
    let expenseRate = 0.8

    let tax1 = Double(prize) * taxRate
    let case1 = prize - Int(round(tax1))

    let tax2 = Double(prize) * (1 - expenseRate) * taxRate
    let case2 = prize - Int(round(tax2))

    return (case1, case2)
}
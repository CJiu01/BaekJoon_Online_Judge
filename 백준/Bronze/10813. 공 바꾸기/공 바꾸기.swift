let countInput = readLine()!.split(separator: " ").map { Int($0)! }
var nums = Array(0...countInput[0])
for _ in 0..<countInput[1] {
    var tmp = 0
    let switchNumber = readLine()!.split(separator: " ").map { Int($0)! }
    tmp = nums[switchNumber[0]]
    nums[switchNumber[0]] = nums[switchNumber[1]]
    nums[switchNumber[1]] = tmp
}

for i in 1..<nums.count {
    print(nums[i], terminator: " ")
}
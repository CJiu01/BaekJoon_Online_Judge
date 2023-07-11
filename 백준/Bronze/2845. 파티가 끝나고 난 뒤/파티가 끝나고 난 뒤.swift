let exactPeopleCount : Int = {
    let input = readLine()!.split(separator: " ").map { Int(String($0))! }
    return input[0] * input[1]
}()

let result = readLine()!.split(separator: " ").map {
    String(Int(String($0))! - exactPeopleCount)
}.joined(separator: " ")
print(result)
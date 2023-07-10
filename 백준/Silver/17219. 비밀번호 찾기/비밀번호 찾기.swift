let input = readLine()!.split(separator: " ").map { Int($0)! }
var siteDictionary: Dictionary<String, String> = [String: String]()

for i in 0..<input[0] {
    let site = readLine()!.split(separator: " ")
    siteDictionary.updateValue(String(site[1]), forKey: String(site[0]))
}

for i in 0..<input[1] {
    let targetSite = readLine()!
    print(siteDictionary[targetSite, default: ""])
}
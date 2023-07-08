import Foundation

var formatter = DateFormatter()
formatter.dateFormat = "yyyy-MM-dd"
var currentDate = formatter.string(from: Date())
print(currentDate)

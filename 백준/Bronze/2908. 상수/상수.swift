let input = readLine()!.split(separator: " ")
let (a,b) = (Int(String(input[0].reversed()))!, Int(String(input[1].reversed()))!)
print(max(a, b))
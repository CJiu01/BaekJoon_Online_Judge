let input = readLine()!.split(separator: " ").map { Int($0)! }
let time = Int(readLine()!)!

var (h,m) = (input[0],input[1])
let tmp = time/60
h += tmp
m += time-(60*tmp)

if m>=60 {
    h += 1
    m %= 60
} 
if h>=24 {
    h %= 24
}

print(h, m)
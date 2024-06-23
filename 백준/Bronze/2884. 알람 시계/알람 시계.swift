let input = readLine()!.split(separator: " ").map { Int($0)! }
var (h, m) = (input[0], input[1])

if (m-45)<0 {
    m = 60-(45-m)
    h -= 1
} else {
    m -= 45
}

if h<0 {
    h = 24+h
}

print(h, m)
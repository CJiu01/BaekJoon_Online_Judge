let value = readLine()!.split(separator: " ").map { Int($0)! }

if value[0]>value[1] {
    print(">")
} else if value[0]<value[1] {
    print("<")
} else {
    print("==")
}
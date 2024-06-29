let tel = ["ABC", "DEF", "GHI", "JKL","MNO","PQRS","TUV","WXYZ"]

let input = readLine()!
var cnt = 0
for i in input {
    for j in 0..<tel.count {
        if tel[j].contains(i) {
            cnt += (j+3)
            break
        }
    }
}
print(cnt)
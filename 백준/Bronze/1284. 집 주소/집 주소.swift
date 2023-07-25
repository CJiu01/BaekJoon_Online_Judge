func solution() {
    while true{
        var input=String(readLine()!)
        if input == "0" {
            break
        }
        var result = input.count+1
        input.forEach {
            if ($0) == "1" {
                result += 2
            } else if ($0) == "0" {
                result += 4
            } else {
                result += 3
            }
        }
        print(result)
    }
}

solution()
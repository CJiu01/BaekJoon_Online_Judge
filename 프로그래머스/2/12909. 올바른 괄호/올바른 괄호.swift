func solution(_ s:String) -> Bool
{
    var stack = ""
    
    for i in s {
        if i == "(" {
            stack.append(i)
        } else {
            if stack.isEmpty {
                return false
            }
            stack.popLast()
        }
    }
    return stack.isEmpty
}
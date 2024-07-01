func solution(_ sizes:[[Int]]) -> Int {
    var row = 0
    var col = 0
    for i in sizes {
        var (a,b) = (i[0],i[1])
        if a<b {
            (a,b) = (b,a)
        }
        row = max(row,a)
        col = max(col,b)
    }
    return row*col
}
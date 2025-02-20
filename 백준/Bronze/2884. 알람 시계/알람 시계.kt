fun main() {
    val (h, m) = readLine()!!.split(" ").map{it.toInt()}
    
    var H = h
    var M = m - 45
    
    if (M < 0) {
        M += 60
        H--
        if (H < 0) {
            H = 23
        }
    }
    println("$H $M")
}

fun main() {
    val (h, m) = readLine()!!.split(" ").map {it.toInt()}
    val Pm = readLine()!!.toInt()
    
    var H = h
    var M = m + Pm
    
    H += M / 60
    M %= 60
    H %= 24
    
    println("$H $M")
}
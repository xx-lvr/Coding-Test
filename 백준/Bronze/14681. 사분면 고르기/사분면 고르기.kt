fun main() {
    val a = readLine()!!.toInt()
    val b = readLine()!!.toInt()
    
    when {
        a > 0 && b > 0 -> println("1")
        a < 0 && b > 0 -> println("2")
        a < 0 && b < 0 -> println("3")
        a > 0 && b < 0 -> println("4")
    }
}
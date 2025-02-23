fun main() {
    val (a, b, c) = readLine()!!.split(" ").map { it.toInt() }

    val prize = when {
        a == b && b == c -> 10000 + a * 1000 
        a == b || a == c -> 1000 + a * 100   
        b == c -> 1000 + b * 100         
        else -> maxOf(a, b, c) * 100        
    }
    println(prize)
}
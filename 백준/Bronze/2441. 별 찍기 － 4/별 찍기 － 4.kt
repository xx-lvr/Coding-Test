fun main() {
    val n = readLine()!!.toInt()

    for (i in n downTo 1) { 
        for (j in 1..n - i) { 
            print(" ")
        }
        for (k in 1..i) { 
            print("*")
        }
        println()
    }
}
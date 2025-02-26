fun main() {
    val a = readLine()!!.toInt() 
    val b = readLine()!! 
    var sum = 0 

    for (i in 0 until a) { 
        sum += b[i].toString().toInt() 
    }
    println(sum)
}
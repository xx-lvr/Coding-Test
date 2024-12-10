fun main() {
    val n = readLine()!!.toInt() 
    var cnt = 0
    var div = 5

    while (n / div > 0) {
        cnt += n / div
        div *= 5
    }
    println(cnt)
}
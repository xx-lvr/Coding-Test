fun main() {
    val a = readLine()!!.toInt()
    val b = readLine()!!.split(" ").map{it.toInt()}
    val c = readLine()!!.toInt()
   
    var count = 0
    for (number in b) {
        if(number == c){
            count++
        }
    }
    println(count)
}
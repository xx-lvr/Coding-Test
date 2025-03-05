import java.io.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    val t = br.readLine().toInt()  

    repeat(t) {
        val (a, b) = br.readLine().split(" ").map { it.toInt() }
        bw.write("${a + b}\n") 
    }

    bw.flush()
    br.close()
    bw.close()
}
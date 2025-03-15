import java.io.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.`out`))

    val n = br.readLine().toInt()

    for (i in 1.. n - 1) {
        for (j in 1..2 * n) {
            if (j <= i || j > 2 * n - i) {
                bw.write("*")
            } else {
                bw.write(" ")
            }
        }
        bw.write("\n")
    }
    for (i in n downTo 1 ) {
        for (j in 2 * n downTo 1) {
            if (j <= i || j > 2 * n - i) {
                bw.write("*")
            } else {
                bw.write(" ")
            }
        }
        bw.write("\n")
    }


    bw.flush()
    bw.close()
}
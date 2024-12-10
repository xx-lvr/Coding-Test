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

/* val n = readLine()!!.toInt(): 입력을 받은 n을 정수로 변환
var cnt = 0: 뒤에 나오는 0의 개수를 셈.
var div = 5: 5의 배수를 확인하는 변수.
while (n / div > 0): 5, 25, 125 등의 배수를 하나씩 확인.
cnt += n / div: 각 배수에서 나오는 0의 개수를 더함.
div *= 5: 5의 배수를 점차 증가시키며 확인. */

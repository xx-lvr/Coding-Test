fun main() {
    val (a, b) = readLine()!!.split(" ").map {it.toInt()}
    println(a * b -1)
}

// 해설
// 여기서 초콜릿은 쪼갤 때마다 1개씩 증가하니 
// 최종적으로 만들어야 하는 조각의 수 (a * b)에서 처음 초콜릿 덩어리 1을 빼면 쪼개야 하는 횟수가 된다

// 예시
/* 입력이 2 3인 경우:
1. a = 2, b = 3
2. a * b - 1 = (2 * 3) - 1 = 6 - 1 = 5
3. 따라서 5를 출력함.
*/

class Solution {
    fun solution(n: Int, k: Int): Int {
        return 12_000 * n + 2_000 * (k - (n / 10))
    }
}
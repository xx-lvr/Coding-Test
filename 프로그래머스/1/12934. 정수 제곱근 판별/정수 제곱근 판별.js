function solution(n) {
    const N = Math.sqrt(n);
    if (Number.isInteger(N)) {
        return (N + 1) ** 2;
    } else {
        return -1;
    }
}
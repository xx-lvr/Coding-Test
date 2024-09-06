function solution(numbers, n) {
    let sum = 0;
    let i = 0;
    while(sum <= n && numbers.length >= i){
        sum += numbers[i];
        i++
    }
    return sum;
}
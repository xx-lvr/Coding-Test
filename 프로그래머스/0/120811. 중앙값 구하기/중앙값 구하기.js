function solution(array) {
    array.sort((a, b) => a - b);
    let mid = array[Math.floor(array.length / 2)];
    return mid;
}
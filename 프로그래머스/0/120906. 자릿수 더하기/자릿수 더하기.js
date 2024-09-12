function solution(n) {
    var arr = n.toString().split("");
    var result = 0;
    for(let i = 0; i < arr.length; i++) {
        result += parseInt(arr[i]);
    }
    return result;
}
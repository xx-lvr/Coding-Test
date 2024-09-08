function solution(array, n) {
    let result = 0;
    for(i = 0; i < array.length; i++){
    if(array[i] === n){
        result++;
    }
  }
    return result;
}
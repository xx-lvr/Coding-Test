function solution(num_list){
    var even = 0;
    var odd = 0;
    for(let i = 0; i < num_list.length; i++){
        if(num_list[i] % 2 == 0){
            even++;
        }
        else
            odd++;
    }
    return [even, odd];
}
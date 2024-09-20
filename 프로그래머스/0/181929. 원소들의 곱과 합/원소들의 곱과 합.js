function solution(num_list) {
    var a = 1, b = 0;
    for(let i = 0; i < num_list.length; i++){
        a *= num_list[i];
        b += num_list[i];
    }
    b = b * b;
    if(a < b){
        return 1;
    }
    else 
        return 0;
}
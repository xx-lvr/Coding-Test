function solution(dot) {
    let x = dot[0] > 0 ? 1 : 0;
    let y = dot[1] > 0 ? 1 : 0;
    return [[3,2],[4,1]][x][y];
}
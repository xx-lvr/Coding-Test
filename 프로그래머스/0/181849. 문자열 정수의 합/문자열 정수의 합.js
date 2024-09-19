function solution(num_str) {
    const num = num_str.split("")
    return num.reduce((a,b)=>a + Number(b),0)
}
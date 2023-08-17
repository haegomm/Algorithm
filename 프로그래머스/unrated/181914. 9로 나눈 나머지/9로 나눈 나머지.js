function solution(number) {
    let num = 0;
    for (let i of number){
        num += Number(i)
    }
    return num % 9;
}
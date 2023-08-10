function solution(n) {
    let num = n;
    const answer = [n]
    while(num > 1) {
        if(num % 2 === 0){
        num =  Math.floor(num/2)
        answer.push(num)
    }else{
        num = 3 * num + 1
        answer.push(num)
    }}
    return answer;
}
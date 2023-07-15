function solution(a, b) {
    var answer = 0;
    const ab = a.toString() + b.toString()
    const num = 2 * a * b
    if(ab >= num){
        answer = Number(ab)
    }else {
        answer = num
    }
    return answer;
}
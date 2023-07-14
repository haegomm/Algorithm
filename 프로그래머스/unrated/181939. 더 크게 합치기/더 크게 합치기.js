function solution(a, b) {
    var answer = 0;
    const  ab = Number(a.toString() + b.toString())
    const ba = Number(b.toString() + a.toString())
    if (ab >= ba){
        answer = ab
    }else {
        answer = ba
    }
    return answer;
}
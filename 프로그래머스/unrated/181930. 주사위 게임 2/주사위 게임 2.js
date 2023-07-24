function solution(a, b, c) {
    let score = a + b + c;
    let square = a*a + b*b + c*c;
    let cube = a*a*a + b*b*b + c*c*c;
    
    if(a === b && b === c) {
        return score * square * cube;
    } else if(a === b || b === c || a === c) {
        return score * square;
    } else {
        return score;
    }
}

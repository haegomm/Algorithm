function solution(r1, r2) {
    let answer = 0;
    for (var x=1;x<=r2;x++) {
        let minY = r1 >= x ? Math.ceil(Math.sqrt(r1*r1-x*x)) : 0;
        let maxY = Math.floor(Math.sqrt(r2*r2-x*x));
        answer += maxY-minY+1;

    }
    return 4*answer;
}

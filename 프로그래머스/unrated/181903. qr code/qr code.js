function solution(q, r, code) {
    let answer = '';
    for(idx = 0; idx < code.length; idx++){
        if(idx % q === r){
            answer += code[idx]
        }
    }
    return answer;
}
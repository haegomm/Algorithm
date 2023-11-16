function solution(my_string, m, c) {
    let answer = '';
    for(let idx = c-1; idx < my_string.length; idx += m){
        answer += my_string[idx];
    }
    return answer;
}
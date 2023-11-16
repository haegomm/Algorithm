function solution(my_string, s, e) {
    let answer = '';
    const splitString = my_string.substring(s,e+1).split('').reverse();
    answer = my_string.substring(0, s) + splitString.join('') + my_string.substring(e+1);
    return answer;
}
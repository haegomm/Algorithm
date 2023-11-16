function solution(my_string, is_prefix) {
    let answer = 0;
    for(let idx = 0; idx < my_string.length; idx++){
        if(is_prefix === my_string.substr(0,idx)){
            answer = 1;
        }
    }
    return answer;
}
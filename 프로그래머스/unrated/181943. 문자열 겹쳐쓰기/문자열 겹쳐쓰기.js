function solution(my_string, overwrite_string, s) {
    var answer = '';
    over_str = overwrite_string.length;
    answer = my_string.substr(0,s) + overwrite_string + my_string.substr(s+over_str)
    return answer;
}
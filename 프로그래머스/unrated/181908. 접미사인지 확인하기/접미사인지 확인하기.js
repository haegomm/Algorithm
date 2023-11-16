function solution(my_string, is_suffix) {
    let answer = 0;
    for(let idx = 0; idx < my_string.length; idx++){
      if(is_suffix === my_string.substr(idx,)){
          answer = 1;
      }
    }
    return answer;
}
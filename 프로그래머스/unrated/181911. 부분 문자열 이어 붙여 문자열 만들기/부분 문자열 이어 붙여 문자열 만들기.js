function solution(my_strings, parts) {
  let result = "";
  for (let i = 0; i < my_strings.length; i++) {
    const [s, e] = parts[i];
    const substring = my_strings[i].slice(s, e + 1);
    result += substring;
  }
  
  return result;
}
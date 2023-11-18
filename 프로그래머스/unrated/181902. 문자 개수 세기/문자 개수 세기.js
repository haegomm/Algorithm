function solution(my_string) {
    let answer = [];

    for(let i = 65; i <= 90; i++){
        const matches = my_string.match(new RegExp(String.fromCharCode(i), 'g')) || [];
        answer.push(matches.length);
    }

    for(let i = 97; i <= 122; i++){
        const matches = my_string.match(new RegExp(String.fromCharCode(i), 'g')) || [];
        answer.push(matches.length);
    }
    return answer;
}

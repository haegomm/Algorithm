function solution(my_string) {
    let answer = [];
    let alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    answer.length = 52;
    answer.fill(0);
    
    my_string.split("").map((word) => {
        answer[alphabet.indexOf(word)] += 1;
    })

    return answer;
}
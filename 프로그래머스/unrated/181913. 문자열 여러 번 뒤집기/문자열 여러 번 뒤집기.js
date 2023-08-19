function solution(my_string, queries) {
    let arr = [...my_string];

    for (let [s, e] of queries) {
        let reversedPart = arr.slice(s, e + 1).reverse();
        arr = [...arr.slice(0, s), ...reversedPart, ...arr.slice(e + 1)];
    }

    return arr.join('');
}
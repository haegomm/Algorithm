function solution(intStrs, k, s, l) {
    let result = [];

    for (let str of intStrs) {
        // s 위치에서 l 길이의 부분 문자열을 잘라냅니다.
        let substring = str.substr(s, l);
        let num = parseInt(substring);

        if (num > k) {
            result.push(num);
        }
    }

    return result;
}
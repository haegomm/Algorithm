function solution(a, b, c, d) {

    let counts = {};
    [a, b, c, d].forEach(num => {
        if (!counts[num]) counts[num] = 0;
        counts[num]++;
    });

    const uniqueNums = Object.keys(counts).map(Number);
    const uniqueCounts = Object.values(counts);

    if (uniqueNums.length === 1) {
        return 1111 * uniqueNums[0];
    } else if (uniqueNums.length === 2) {
        if (uniqueCounts.includes(3)) {
            let threeNum = uniqueNums[uniqueCounts.indexOf(3)];
            let oneNum = uniqueNums[uniqueCounts.indexOf(1)];
            return (10 * threeNum + oneNum) ** 2;
        } else {
            let firstNum = uniqueNums[0];
            let secondNum = uniqueNums[1];
            return (firstNum + secondNum) * Math.abs(firstNum - secondNum);
        }
    } else if (uniqueNums.length === 3) { 
        let doubleNum = uniqueNums[uniqueCounts.indexOf(2)];
        let singles = uniqueNums.filter(num => num !== doubleNum);
        return singles[0] * singles[1];
    } else {
        return Math.min(a, b, c, d);
    }
}
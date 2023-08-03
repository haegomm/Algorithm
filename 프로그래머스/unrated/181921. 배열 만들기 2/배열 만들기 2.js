function solution(l, r) {
    const arr = [];
    const queue = ["5"];
    while (queue.length > 0) {
        const numStr = queue.shift();
        const num = parseInt(numStr, 10);
        if (num >= l && num <= r) {
            arr.push(num);
        }
        if (num > r) {
            break;
        }
        queue.push(numStr + "0");
        queue.push(numStr + "5");
    }
    return arr.length ? arr.sort((a,b)=>a-b) : [-1];
}
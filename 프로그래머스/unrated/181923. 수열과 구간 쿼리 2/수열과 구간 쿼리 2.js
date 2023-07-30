function solution(arr, queries) {
    const answer = [];
    
    for(let [s, e, k] of queries){
        const subArr = arr.slice(s, e + 1).filter(num => num > k).sort((a, b) => a - b);
        
        if (subArr.length === 0){
            answer.push(-1);
        } else {
            answer.push(subArr[0]);
        }
    }
    
    return answer;
}
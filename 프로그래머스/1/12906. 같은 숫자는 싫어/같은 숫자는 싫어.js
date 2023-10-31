function solution(arr)
{   const answer = []
    let now = arr[0];
    answer.push(now)
    for (let i = 1; i < arr.length; i++){
        if (now !== arr[i]){  
            now = arr[i]
            answer.push(arr[i])
        }
    }
    return answer;
}
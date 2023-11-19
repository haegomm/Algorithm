function solution(targets) {
    targets.sort((a, b) => a[1] - b[1]);
    let cnt = 0;
    let lastEnd = -1;
    
    for(const target of targets){
        if(lastEnd <= target[0]){
            lastEnd = target[1];
            cnt += 1;
        }
    }
    return cnt;
}
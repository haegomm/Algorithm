function solution(name, yearning, photo) {
    let answer = [];
    let yearningPoint = {};
    name.forEach((person, idx) => {
        yearningPoint[person] = yearning[idx];
    })
    for (people of photo) {
        let sumPoint = 0;
        for (man of people) {
            if (yearningPoint[man]){
                sumPoint += yearningPoint[man];
            }
        }
        answer.push(sumPoint);
    }
    return answer;
}
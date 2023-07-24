function solution(num_list) {
    let sum = num_list.reduce((acc, num) => acc + num, 0);
    let mul = num_list.reduce((acc, num) => acc * num, 1);
    return (sum**2 > mul ? 1 : 0);
}
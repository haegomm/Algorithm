function solution(num_list) {
    const last = num_list[num_list.length - 1];
    if(last > num_list[num_list.length - 2]){
        num_list.push(last - num_list[num_list.length - 2])
    }else {
        num_list.push(last * 2)
    }
    return num_list;
}

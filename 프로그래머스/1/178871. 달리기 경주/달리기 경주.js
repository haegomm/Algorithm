function solution(players, callings) {
    let position = {};
    players.forEach((player, index) => {
        position[player] = index;
    });
    
    callings.forEach(calling => {
        let currIndex = position[calling];
        [players[currIndex], players[currIndex - 1]] = [players[currIndex - 1], players[currIndex]];
        position[players[currIndex]] = currIndex;
        position[calling] = currIndex - 1;
    })
    return players;
}
def solution(players, callings):
    position = {name: i for i, name in enumerate(players)}

    for name in callings:
        curr_pos = position[name]
        players[curr_pos], players[curr_pos - 1] = players[curr_pos - 1], players[curr_pos]

        position[players[curr_pos]] = curr_pos
        position[name] = curr_pos - 1

    return players
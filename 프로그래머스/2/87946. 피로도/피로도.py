from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0
    for perm in permutations(dungeons):
        current_stamina = k
        visited_dungeons = 0
        for dungeon in perm:
            required_stamina, consumed_stamina = dungeon
            if current_stamina >= required_stamina:
                current_stamina -= consumed_stamina
                visited_dungeons += 1
            else:
                break
        max_dungeons = max(max_dungeons, visited_dungeons)
    return max_dungeons
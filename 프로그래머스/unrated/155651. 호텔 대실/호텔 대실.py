def solution(book_time):
    def change(reservation_time):
        return int(reservation_time[0:2]) * 60 + int(reservation_time[3:])

    reservations = []
    for time in book_time:
        reservations.append([change(time[0]), change(time[1]) + 10])

    reservations.sort()

    hotel_rooms = []
    for reservation in reservations:
        if not hotel_rooms:
            hotel_rooms.append(reservation)
            continue
        for idx, room in enumerate(hotel_rooms):
            if reservation[0] >= room[-1]:
                hotel_rooms[idx] = room + reservation
                break
        else:
            hotel_rooms.append(reservation)
    return len(hotel_rooms)
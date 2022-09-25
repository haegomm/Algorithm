for t in range(1, int(input()) + 1):
    n = int(input())
    stations = [0] * 5001
    result = []

    for _ in range(n):
        a, b = map(int, input().split())

        for i in range(a, b+1):
            stations[i] += 1

    p = int(input())

    for _ in range(p):
        j = int(input())
        result.append(stations[j])

    print(f'#{t}', *result)
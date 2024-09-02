n = int(input())
infos = [input().split() for _ in range(n)]

infos = [[int(age), name] for age, name in infos]

infos.sort(key=lambda info: info[0])

for info in infos:
    print(info[0], info[1])

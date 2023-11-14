n, m = map(int, input().split())
dna_list = [input() for _ in range(n)]

ans_dna = ''
min_hamming_distance = 0

for i in range(m):
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for dna in dna_list:
        count[dna[i]] += 1
    most_nucleo = max(count, key=count.get)
    ans_dna += most_nucleo
    for nucleo in count:
        if nucleo != most_nucleo:
            min_hamming_distance += count[nucleo]

print(ans_dna)
print(min_hamming_distance)
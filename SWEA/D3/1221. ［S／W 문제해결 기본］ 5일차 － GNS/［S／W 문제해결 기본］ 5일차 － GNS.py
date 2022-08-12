planet_numbers = ['ZRO', 'ONE', 'TWO', 'THR',
                  'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

t = int(input())


for tc in range(1, t + 1):

    tc_num, case_len = input().split()
    case_len = int(case_len)

    mix_numbers = input()

    for i in range(10):
        mix_numbers = mix_numbers.replace(planet_numbers[i], str(i))

    mix_numbers = ' '.join(sorted(mix_numbers))
    mix_numbers = mix_numbers.strip(' ')

    for j in range(10):
        mix_numbers = mix_numbers.replace(str(j), planet_numbers[j])

    print(f'#{tc}')
    print(mix_numbers)
# index 사용
def solution(neo_num):

    number_english = ['zero', 'one', 'two', 'three',
                      'four', 'five', 'six', 'seven', 'eight', 'nine']
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for e_idx in range(10):
        if neo_num.find(e_idx):
            neo_num = neo_num.replace(number_english[e_idx], number[e_idx])

    return neo_num


# enumerate 사용
def solution(neo_num):

    number_english = ['zero', 'one', 'two', 'three',
                      'four', 'five', 'six', 'seven', 'eight', 'nine']

    for idx, e_num in enumerate(number_english):
        neo_num = neo_num.replace(e_num, str(idx))

    return int(neo_num)

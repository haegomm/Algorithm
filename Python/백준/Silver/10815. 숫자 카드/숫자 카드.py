import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

card_dict = {card: 1 for card in cards}

for num in nums:
    if num in card_dict:
        print(1, end=' ')
    else:
        print(0, end=' ')
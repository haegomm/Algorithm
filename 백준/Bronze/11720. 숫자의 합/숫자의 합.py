import sys

input = sys.stdin.readline

n = input()
words = [int(char) for char in input().strip()]
print(sum(words))
tc = int(input())
temp = input()
num_lst = [0] * tc

for t in range(tc):
    num_lst[t] = int(input())

stack = []

for i in temp:
    if 'A' <= i <= 'Z':
        stack.append(num_lst[ord(i) - ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)

print('%.2f' % stack[0])
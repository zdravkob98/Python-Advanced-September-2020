first_line = [int(x) for x in input().split(', ')]
second_line = int(input())

total = 0
flag = False

while True:
    m = min(first_line)
    idx = first_line.index(m)

    if idx == second_line:
        flag = True
    if idx < second_line:
        second_line -= 1

    n = first_line.pop(idx)
    total += n

    if flag:
        break


print(total)

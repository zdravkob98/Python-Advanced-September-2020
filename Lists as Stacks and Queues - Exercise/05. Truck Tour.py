from _collections import deque

n = int(input())
pumbs = deque()
copy = []

for _ in range(n):
    pumb = [int(x) for x in input().split()]
    pumbs.append(pumb)

fuel = 0

for i in range(n):
    is_valid = True
    fuel = 0

    for _ in range(n):
        current = pumbs.popleft()
        fuel += current[0] - current[1]
        if fuel < 0:
            is_valid = False
        pumbs.append(current)

    if is_valid:
        print(i)
        break

    pumbs.append(pumbs.popleft())
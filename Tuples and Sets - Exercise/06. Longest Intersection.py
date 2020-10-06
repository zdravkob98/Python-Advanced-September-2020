n = int(input())

a_set = set()
b_set = set()

intersection = set()
current = set()

for _ in range(n):
    a_set.clear()
    b_set.clear()
    current.clear()

    token = input().split('-')
    a = token[0].split(',')
    a_start = int(a[0])
    a_end = int(a[1])

    b = token[1].split(',')
    b_start = int(b[0])
    b_end = int(b[1])

    for i in range(a_start, a_end + 1):
        a_set.add(i)

    for i in range(b_start, b_end + 1):
        b_set.add(i)


    match = a_set.intersection(b_set)


    current = current.union(match)
    if len(current) > len(intersection):
        intersection = current.copy()

intersection_str = list(intersection)
print(f"Longest intersection is {intersection_str} with length {len(intersection)}")
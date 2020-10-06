n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name = input()
    total = 0
    for char in name:
       total += ord(char)
    total = total // i
    if total % 2 == 0:
        even_set.add(total)
    else:
        odd_set.add(total)

sum_odd = sum(odd_set)
sum_even = sum(even_set)

if sum_even == sum_odd:
    union = map(str, odd_set.union(even_set))
    print(', '.join(union))
elif sum_even > sum_odd:
    symmetric_different_values = map(str, odd_set.symmetric_difference(even_set))
    print(', '.join(symmetric_different_values))
elif sum_even < sum_odd:
    different_values = map(str, odd_set.difference(even_set))
    print(', '.join(different_values))
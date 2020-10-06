from itertools import permutations
text = input()

perm = permutations(text)

for i in perm:
    print(''.join(i))
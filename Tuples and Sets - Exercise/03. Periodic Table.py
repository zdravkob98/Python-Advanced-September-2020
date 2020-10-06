n = int(input())

compounds = set()

for _ in range(n):
    token = input().split(' ')
    while token:
        compound = token[0]
        compounds.add(compound)
        token.remove(compound)
print('\n'.join(compounds))
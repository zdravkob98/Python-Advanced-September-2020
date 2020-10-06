count = int(input())

names = set()

for _ in range(count):
    username = input()
    names.add(username)

print('\n'.join(names))
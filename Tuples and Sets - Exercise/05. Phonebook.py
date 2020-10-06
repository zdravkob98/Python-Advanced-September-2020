from _collections  import defaultdict

phonebook = defaultdict(str)

search = input()
while True:
    if search.isdigit():
        break
    else:
        token = search.split('-')
        name = token[0]
        number = token[1]
        phonebook[name] = number
    search = input()

n = int(search)
for _ in range(n):
    phone_name = input()
    if phone_name in phonebook:
        print(f'{phone_name} -> {phonebook[phone_name]}')
    else:
        print(f"Contact {phone_name} does not exist.")
reservation = int(input())

people_nums = set()

for _ in range(reservation):
    r_number = input()
    people_nums.add(r_number)

while True:
    person = input()

    if person == 'END':
        break
    else:
        if person in people_nums:
            people_nums.remove(person)

people_nums = sorted(people_nums)
print(len(people_nums))
print('\n'.join(people_nums))
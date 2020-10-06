count_command = int(input())

parking = set()

for _ in range(count_command):
    token = input().split(', ')
    command, number = token
    if command == 'IN':
        parking.add(number)
    elif command == 'OUT':
        if number in parking:
            parking.remove(number)

if not parking:
    print('Parking Lot is Empty')
else:
    print('\n'.join(parking))
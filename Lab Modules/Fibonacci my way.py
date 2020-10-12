import fibonccimodule

last_fibonacci = ''
while True:
    command = input().split()

    if command[0] == 'Stop':
        break

    elif command[0] == 'Create':
        count = int(command[-1])
        last_fibonacci = list(map(str,fibonccimodule.create_fibonacci(count)))
        print(' '.join(last_fibonacci))

    elif command[0] == 'Locate':
        number = command[1]
        index = None
        for n in last_fibonacci:
            if n == number:
                index = last_fibonacci.index(n)
        if index is None:
            print(f'The number {number} is not in the sequence')
        else:
            print(f'The number - {number} is at index {index}')


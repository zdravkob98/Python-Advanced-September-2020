from _collections import deque

green_windows = int(input())
free_windows = int(input())

timer_green = green_windows
timer_free = free_windows

cars = deque()

crash = False
save_cars = 0
char = ''
last_car = ''

command = input()
while command != 'END':
    if command == 'green':
        if cars:
            current = cars.popleft()
            last_car = current
            current_car = deque(current)
            for s in range(green_windows + free_windows):
                if timer_green > 0:
                    timer_green -= 1
                    current_car.popleft()
                    if not current_car:
                        save_cars += 1
                        if cars and timer_green > 0:
                            current = cars.popleft()
                            last_car = current
                            current_car = deque(current)
                        else:
                            timer_green = green_windows
                            timer_free = free_windows
                            break
                if timer_green == 0:
                    if timer_free > 0:
                        timer_free -= 1
                        current_car.popleft()
                        if not current_car:
                            save_cars += 1
                            timer_green = green_windows
                            timer_free = free_windows
                            break

                    elif current_car:
                        crash = True
                        char = current_car.popleft()
                        break
    else:
        cars.append(command)
    if crash:
        break
    command = input()

if crash:
    print('A crash happened!')
    print(f'{last_car} was hit at {char}.')
else:
    print('Everyone is safe.')
    print(f'{save_cars} total cars passed the crossroads.')

from _collections import deque

cups = deque([int(x) for x in input().split()])
bottle = [int(x) for x in input().split()]

wasted_water = 0

while True:
    if not cups:
        break
    elif not bottle:
        break

    current_bottle = bottle.pop()
    current_cup = cups.popleft()

    if current_bottle >= current_cup:
         wasted_water += current_bottle - current_cup
    else:
        current_cup -= current_bottle
        cups.appendleft(current_cup)

if not cups:
    print(f'Bottles: {" ".join(map(str, bottle[::-1]))}')
    print(f"Wasted litters of water: {wasted_water}")
else:
    print(f'Cups: {" ".join(map(str, cups))}')
    print(f"Wasted litters of water: {wasted_water}")
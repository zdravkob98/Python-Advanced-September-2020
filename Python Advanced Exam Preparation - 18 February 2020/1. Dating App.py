from _collections import deque

male = [int(x) for x in input().split()]
female = deque([int(x) for x in input().split()])

matches = 0

while True:
    if not male or not female:
        break

    current_female = female.popleft()
    current_male = male.pop()

    if current_female <= 0 :
        male.append(current_male)
        continue
    if current_male <= 0:
        female.appendleft(current_female)
        continue

    if current_female % 25 == 0:
        male.append(current_male)
        if female:
            female.popleft()
        continue
    if current_male % 25 == 0:
        female.appendleft(current_female)
        if male:
            male.pop()
        continue

    if current_female == current_male:
        matches += 1
        continue
    else:
        male.append(current_male - 2)

print(f'Matches: {matches}')
if male:
    print(f"Males left: {', '.join(map(str, reversed(male)))}")
else:
    print('Males left: none')
if female:
    print(f'Females left: {", ".join(map(str, female))}')
else:
    print('Females left: none')
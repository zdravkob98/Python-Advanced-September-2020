from _collections import deque

bomb_effect = deque(input().split(', '))
bomb_casing = input().split(', ')

datura_bombs = 40
cherry_bombs = 60
smoke_decoy_bombs = 120

dict = {'Datura_Bombs' : 0, 'Cherry_Bombs' : 0, 'Smoke_Decoy_Bombs' : 0}
flag = False
while True:
    if len(bomb_effect) == 0:
        break
    if len(bomb_casing) == 0:
        break
    d_bomb = dict['Datura_Bombs']
    c_bomb = dict['Cherry_Bombs']
    s_bomb = dict['Smoke_Decoy_Bombs']
    if d_bomb >= 3 and c_bomb >= 3 and s_bomb >= 3:
        flag = True
        break
    current_bomb_effect = int(bomb_effect.popleft())
    current_bomb_casing = int(bomb_casing.pop())

    bomb_sum = current_bomb_effect + current_bomb_casing

    if bomb_sum == datura_bombs:
        dict['Datura_Bombs'] += 1
    elif bomb_sum == cherry_bombs:
        dict['Cherry_Bombs'] += 1
    elif bomb_sum == smoke_decoy_bombs:
        dict['Smoke_Decoy_Bombs'] += 1
    else:
        bomb_effect.appendleft(current_bomb_effect)
        bomb_casing.append(current_bomb_casing - 5)



if flag:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print(f"Bomb Effects: {', '.join(bomb_effect)}")
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f"Bomb Casings: {', '.join(bomb_casing)}")
else:
    print("Bomb Casings: empty")

for k, v in sorted(dict.items()):
    if k == 'Cherry_Bombs':
        print(f'Cherry Bombs: {v}')
    if k == 'Datura_Bombs':
        print(f'Datura Bombs: {v}')
    if k == 'Smoke_Decoy_Bombs':
        print(f'Smoke Decoy Bombs: {v}')

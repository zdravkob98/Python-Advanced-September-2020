from _collections import deque

price_of_each_bullet = int(input())
size_of_the_gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
value_of_intelligence = int(input())

counter = 0
bullets_count = 0
while True:

    if not bullets:
        break
    elif not locks:
        break

    current_bullet = bullets.pop()
    bullets_count += 1
    counter += 1
    current_lock = locks.popleft()

    if current_bullet <= current_lock:
        print('Bang!')
    else:
        locks.appendleft(current_lock)
        print('Ping!')

    if bullets_count == size_of_the_gun_barrel and bullets:
        print(f'Reloading!')
        bullets_count = 0


if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    value_of_intelligence -= counter * price_of_each_bullet
    print(f"{len(bullets)} bullets left. Earned ${value_of_intelligence}")
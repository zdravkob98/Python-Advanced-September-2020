from collections import deque

customer = deque(map(int,(input().split(', '))))
taxis = [int(x) for x in input().split(', ')]

total_time = 0

while customer and taxis:
    current_customer = customer.popleft()
    current_taxi = taxis.pop()

    if current_taxi < current_customer:
        customer.appendleft(current_customer)
    else:
        total_time += current_customer

if customer:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(map(str, customer))}')
else:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
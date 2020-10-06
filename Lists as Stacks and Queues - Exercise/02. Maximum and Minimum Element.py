n = int(input())

stack_numbers = []
for _ in range(n):
    tokens = input().split(' ')
    command = int(tokens[0])

    if command == 1:
        stack_numbers.append(int(tokens[1]))
    elif command == 2:
        if len(stack_numbers) > 0:
            stack_numbers.pop()
    elif command == 3:
        if len(stack_numbers) > 0:
            print(max(stack_numbers))
    elif command == 4:
        if len(stack_numbers) > 0:
            print(min(stack_numbers))

final_stack = []
while stack_numbers:
    final_stack.append(stack_numbers.pop())
final_stack = list(map(str, final_stack))
print(', '.join(final_stack))


#print(', '.join([str(x) for x in reversed(st
# ack_numbers)]))
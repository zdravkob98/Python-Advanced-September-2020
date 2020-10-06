list = input().split(' ')

stack = []

while list:
    manipulation = list.pop()
    stack.append(manipulation)
print(' '.join(stack))

# list = input().split(' ')
#
# stack = []
#
# while list:
#
#     stack.append(list.pop())
# print(' '.join(stack))
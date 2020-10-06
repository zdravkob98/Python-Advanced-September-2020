string = input()

stack = []

for char in string:
    stack.append(char)

reversed = ''
while len(stack) > 0:
    item = stack.pop()
    reversed += item

print(reversed)

#stack = list(input())

#reversed = ''
#while len(stack) > 0:
    #item = stack.pop()
    #reversed += item

#print(reversed)


# string = list(input())
# new_string = reversed(string)
# print(list(new_string))


# string = list(input())
# new_string = string[::-1]
# print(new_string)
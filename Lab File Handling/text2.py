file = open('asd.txt', 'w')
file.write('hello\n')
file.close()

# file = open('asd.txt', 'r')
# print(file.read())

with open('asd.txt', 'a') as writing:
    writing.write("Hello World!!!")
with open('asd.txt', 'r') as reading:
    print(reading.read())



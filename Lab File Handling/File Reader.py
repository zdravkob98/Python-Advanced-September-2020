sum = 0
file = open(r'C:\Users\zdravkob\Desktop\08-File-Handling-Lab-Resources\File Reader\numbers.txt', 'r')
for line in file:
    sum += int(line)

print(sum)
text = input().split('|')[::-1]

result = [char for x in text for char in x.split(' ') if char != '']

print(' '.join(result))
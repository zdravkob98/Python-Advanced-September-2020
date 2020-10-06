token = input().split(' ')
n = int(token[0])
m = int(token[1])

n_set = set()
m_set = set()

for i in range(n):
    num = int(input())
    n_set.add(num)

for i in range(m):
    number = int(input())
    m_set.add(number)


result = map(str, n_set & m_set)
print('\n'.join(result))
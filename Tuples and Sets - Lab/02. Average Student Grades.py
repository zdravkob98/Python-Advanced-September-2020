from _collections import defaultdict

n = int(input())
dict = defaultdict(list)

for i in range(n):
    tolken = input().split(' ')
    name = tolken[0]
    grade = float(tolken[1])

    dict[name].append(grade)

for k,v in dict.items():
    average = format(sum(v) / len(v), '.2f')
    mark_str = ' '.join(map(lambda f: format(f, '.2f'), v))
    print(f'{k} -> {mark_str} (avg: {average})')
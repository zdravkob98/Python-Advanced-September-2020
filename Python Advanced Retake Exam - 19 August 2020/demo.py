l = [1, 2, 1,  3, 4]

for i in range(len(l)):
    if i + 1 < len(l):
        if l[i] + 1 != l[i + 1]:
            print('missing')
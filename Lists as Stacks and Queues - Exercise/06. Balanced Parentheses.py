text = input()
par = []
parentheses = {'(': ')', '{': '}', '[': ']'}
status = True
for i in text:
    if i in parentheses:
        par.append(i)
    else:
        if len(par) == 0:
            status = False
            break
        paren = par.pop()
        if parentheses[paren] != i:
            status = False
            break
if status is True and len(par) == 0:
    print('YES')
else:
    print('NO')
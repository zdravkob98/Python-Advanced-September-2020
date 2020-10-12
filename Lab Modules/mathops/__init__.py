import operator

operation = {
    '/' : operator.truediv,
    '*' : operator.mul,
    '-' : operator.sub,
    '+' : operator.add,
    '^' : operator.pow,
}


def result(sign, n1, n2):
    print(operation[sign](n1, n2))
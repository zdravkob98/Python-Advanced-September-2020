from _collections import deque
import operator
import math

def procesing(result, char):
    if char == '-':
        current_result = result.popleft()
        while result:
            current_result -= result.popleft()
        result.append(current_result)
    elif char == '+':
        current_result = result.popleft()
        while result:
            current_result += result.popleft()
        result.append(current_result)
    elif char == '*':
        current_result = result.popleft()
        while result:
            current_result *= result.popleft()
        result.append(current_result)
    elif char == '/':
        current_result = result.popleft()
        while result:
            current_result /= result.popleft()
        result.append(math.floor(current_result))

expression = deque(input().split())
operation = '+-*/'

result = deque()

while expression:
    char = expression.popleft()

    if char in operation:
        procesing(result, char)
    else:
        result.append(int(char))

print(' '.join(map(str,result)))
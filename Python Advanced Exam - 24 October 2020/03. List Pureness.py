from collections import deque

def best_list_pureness (list, k):

    rotation = k + 1
    final_sum = 0
    final_k = 0
    sum = 0
    list = deque(list)

    for i in range(rotation):
        if i != 0:
            last = list.pop()
            list.appendleft(last)
        sum = 0
        for j in range(len(list)):
            sum += list[j] * j
        if sum > final_sum:
            final_sum = sum
            final_k = i


    return f"Best pureness {final_sum} after {final_k} rotations"






test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)



from collections import deque

def list_manipulator (list, second, third, *args):

    finall_list = deque()

    if second == 'remove':
        if third == 'beginning':
            for n in list:
                finall_list.append(n)
            if args:
                for i in range(args[0]):
                    finall_list.popleft()
            else:
                finall_list.popleft()

        elif third == 'end':
            for n in list:
                finall_list.append(n)
            if args:
                for i in range(args[0]):
                    finall_list.pop()
            else:
                finall_list.pop()

    elif second == 'add':
        if third == 'beginning':
            for n in args:
                finall_list.append(n)
            for n in list:
                finall_list.append(n)
        if third == 'end':
            for n in list:
                finall_list.append(n)
            for n in args:
                finall_list.append(n)


    my_list = []
    for obj in finall_list:
        my_list.append(obj)
    return my_list
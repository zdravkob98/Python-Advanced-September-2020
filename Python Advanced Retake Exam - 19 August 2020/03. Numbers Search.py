def numbers_searching (*nums):
    current_list = []
    duplicate = set()
    final_list = []

    for idx in nums:
        current_list.append(idx)

    current_list = sorted(current_list)
    flag = True

    for i in range(len(current_list)):
        flag = True
        # duplicate
        if current_list[i] in current_list[i + 1:]:
            duplicate.add(current_list[i])
            flag = False
        if flag:
            #missing
            if i + 1 < len(current_list):
                if current_list[i] + 1 != current_list[i + 1]:
                    final_list.append(current_list[i] + 1)

    duplicate = sorted(list(duplicate))
    final_list.append(duplicate)
    return final_list





print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

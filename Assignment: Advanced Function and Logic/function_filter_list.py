my_list = [2, 10, 17, 43, 9, 14, 31, 22, 7, 1, 21]
threshold = 20

def func(my_list, threshold):
    modified_list = []

    for item in my_list:
        if item <= threshold:
            modified_list.append(item)

    return modified_list

print(func(my_list, threshold))

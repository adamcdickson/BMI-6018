my_list = [10, 11, 12, 13, 14, [15, 16, 17, [18, 19]]]

def recursive_func(inner_list):
    for item in inner_list:
        if isinstance(item, list):
            return recursive_func(item)

    return_list = []

    for item in inner_list:
        return_list.append(item + 1)
    return return_list

recursive_func(my_list)

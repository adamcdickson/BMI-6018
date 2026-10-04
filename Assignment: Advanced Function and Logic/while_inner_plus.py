my_list = [10, 11, 12, 13, 14, [15, 16, 17, [18, 19]]]
current_list = my_list
i = 0

while i < len(current_list):
    if isinstance(current_list[i], list):
        current_list = current_list[i]
        i = 0
    else:
        i = i + 1

return_list = []
i = 0

while i < len(current_list):
    return_list.append(current_list[i] + 1)
    i = i + 1

print(return_list)
def check_list(list1, element):
    for i in range(len(list1)):
        element_is_in_list = False
        if list1[i] == element:
            element_is_in_list = True
            break

    return element_is_in_list


List = [1, 2, 3, 5, 6, 7, 88, 9]
print(check_list(List, 1209))

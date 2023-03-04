def contains_odd(input_list):
    for number in input_list:
        if number % 2 == 1:
            return True
    return False
        
def is_odd(input_list):
    isodd_list = []

    for number in input_list:
        isodd_list.append(number % 2 == 1)

    return isodd_list

def element_wise_sum(input_list_1, input_list_2):
    wisesum_list = []
        
    list1 = list(input_list_1)
    list2 = list(input_list_2)

    if len(list1) < len(list2):
        list1 += [0] * (len(list2) - len(list1))
    else:
        list2 += [0] * (len(list1) - len(list2))


    wisesum_list = [sum(value) for value in zip(list1, list2)]

    return wisesum_list

def dict_to_list(input_dict):
    tupleslist = []

    for (key, value) in input_dict:
        tupleslist.append((key, value))

    return tupleslist
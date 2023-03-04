def subset(input_list, start_index, end_index):
    sublist = []

    for index in range(start_index, end_index): #end_index inclusive or exclusive?
        sublist.append(input_list[index])

    return sublist

def every_nth(input_list, step_size):
    
    nthlist = []

    nth_index = 1

    for element in input_list:
        if(nth_index == step_size):
            nthlist.append(element)
            nth_index = 1
        else:
            nth_index += 1

    return nthlist

def unique(input_list):
    return len(input_list) == len(set(input_list))

def flatten(input_list):
    output_list = []

    for list in input_list:
        for element in list:
            output_list.append(element)

    return output_list

def merge_lists(*args):
    merged_list = []

    for arg in args:
        merged_list.extend(arg)

    return merged_list

def reverse_tuples(input_list):
    reversed_list = []

    for element in input_list:
        reversed_list.append(tuple(reversed(element)))

    return reversed_list

def remove_tuplicates(input_list):
    return set(input_list)

def transpose(input_list):
    transposed = []

    transposed.append(list(zip(*input_list)))

    return transposed

def split_into_chunks(input_list, chunk_size):
    chunks = []

    chunks = [input_list[i:i+chunk_size] for i in range(0, len(input_list), chunk_size)]
    
    return chunks

def merge_dicts(*dict):
    merged_dicts = {}

    for d in dict:
        merged_dicts.update(d)

    return merged_dicts

def by_parity(input_list):
    dic_parity = {"even":[], "odd":[]}

    for element in input_list:
        if(element % 2 == 0):
            dic_parity["even"].append(element)
        else:
            dic_parity["odd"].append(element)

    return dic_parity

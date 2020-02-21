def get_key(dict, item):
    for key, value in dict.items():
        if value == item:
            return key


def split_list_on_index(data_list, index_list):
    all_index = (0,) + tuple(data + 1 for data in index_list) + (len(data_list),)
    all_lists = []
    for start, end in zip(all_index, all_index[1:]):
        all_lists.append(data_list[start:end])
    return all_lists


def split_list_of_product(list, attribute):
    index_list = []
    for index, product in enumerate(list[:-1]):
        value_0 = list[index].get_value(attribute)
        value_1 = list[index + 1].get_value(attribute)
        if value_0 != value_1:
            index_list.append(index)
    list_of_lists = split_list_on_index(list, index_list)
    return list_of_lists

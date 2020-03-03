import urllib.request
from database.functions_db import *

def get_key(dict, item):
    """
    Find the key for an item value in a dictionnary
    :param dict: a dictionnary {}
    :param item: the value we want to find (string)
    :return: the key corresponding to the item
    """
    for key, value in dict.items():
        if value == item:
            return key


def split_list_on_index(data_list, index_list):
    """
    Split a list of data on multiple index
    :param data_list: a list of data []
    :param index_list: a list of index []
    :return: a list of sub-list [[]]
    """
    all_index = (0,) + tuple(data + 1 for data in index_list) + (len(data_list),)
    all_lists = []
    for start, end in zip(all_index, all_index[1:]):
        all_lists.append(data_list[start:end])
    return all_lists


def split_list_of_product(list, attribute):
    """
    Split a list of Product objects on a attribute
    :param list: a list of Product objects []
    :param attribute: the name of the attribute
    :return: a dictionnary {'lists':[], 'values':[]}
    lists = a list of sub-lists of the products
    values = the value of the attribute for each sublist of products
    """
    if attribute == "name":
        interesting = get_all("Produits_interessants", "nom")
        dict_excel = {"lists": [], "values": []}

        for substring in interesting:
            substring_in = []
            other = []
            for product in list:
                if substring in product.name:
                    substring_in.append(product)
                else:
                    other.append(product)
            dict_excel["lists"].append(substring_in)
            dict_excel["values"].append(substring)
            list = other

        dict_excel["lists"].append(list)
        dict_excel["values"].append("others")

        return dict_excel

    else:
        index_list = []
        values_of_attribute = [list[0].get_value(attribute)]
        for index, product in enumerate(list[:-1]):
            value_0 = list[index].get_value(attribute)
            value_1 = list[index + 1].get_value(attribute)
            if value_0 != value_1:
                index_list.append(index)
                values_of_attribute.append(value_1)
        list_of_lists = {}
        list_of_lists["lists"] = split_list_on_index(list, index_list)
        list_of_lists["values"] = values_of_attribute
        return list_of_lists


def connected_to_internet(url):
    """
    Check connection to Internet
    :param url : the url you want to test
    :return a dictionnary {'connected':bool, 'error':string}
    """
    try:
        urllib.request.urlopen(url)
        return {'connected':True, 'error':None}
    except Exception as e:
        return {'connected':False, 'error':str(e)}


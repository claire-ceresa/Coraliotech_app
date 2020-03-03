import sqlite3 as s
import urllib.request

local_database = "database\coraliotech_db.db" # the name of the local database
# local_database = "database\coraliotech_test_db.db" # the name of the local database


def commit_query(query):
    """
    Commiting a query on the local database
    :param query : MySQL query
    :return a dictionnary {'commited':bool, 'error':string}
    """
    try:
        connection = s.connect(local_database)
        cursor = connection.cursor()
        cursor.execute("pragma foreign_keys = ON")
        cursor.execute(query)
        connection.commit()
        connection.close()
        return {'commited':True, 'error':''}
    except Exception as e:
        return {'commited':False, 'error':str(e)}


def execute_query(query):
    """
    Executing a query on the local database
    :param query : MySQl query
    :return a list of the RAW results []
    """
    connection = s.connect(local_database)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result


def get_query_insert(table, datas):
    """
    Creating a query, type INSERT INTO
    :param table : the name of the table
    :param datas : a dictionnary {attribute:value}
    :return the query (string)
    """
    begin = "INSERT INTO " + table + " ( "
    keys = (" , ").join(datas.keys())
    middle = " ) VALUES ( "
    values = (" , ").join(list(datas.values()))
    end = " );"
    query = begin + keys + middle + values + end
    return query


def get_product_by(id=None, name=None):
    """
    Getting all the information for a Product, not deleted
    :param id: the GenBank identifiant of the product
    :param name: the name of the product
    :return a dict, with all the value of the product {'attribute':value}
    """
    if id is not None:
        query = "SELECT * FROM Produit WHERE id =\"" + id + "\" AND is_delete = 0;"
    elif name is not None:
        query = "SELECT * FROM Produit WHERE nom =\"" + name + "\" AND is_delete = 0;"
    else:
        return ValueError

    result = execute_query(query)
    dict_result = {}

    if len(result) == 1:
        dict_result["id"] = result[0][0]
        dict_result["name"] = result[0][1]
        dict_result["predicted"] = result[0][2]
        dict_result["is_delete"] = result[0][3]
        dict_result["source"] = result[0][4]
        dict_result["note"] = result[0][5]
        dict_result["species"] = result[0][6]
        dict_result["cds_id"] = result[0][7]
        dict_result["fonction"] = result[0][8]

    return dict_result


def get_cds_by(id_cds=None, id_product=None):
    """
    Get all the information for a CDS
    :param id_cds: the identifiant of the cds (as saved on the DB)
    :param id_product : the GenBank of the product corresponding to the cds
    :return a dict with all the value of the cds {'attribute':value}
    """
    if id_product is not None:
        id_cds = "cds_" + id_product

    query = "SELECT * FROM CDS WHERE id = \"" + id_cds + "\" AND is_delete = 0"
    result = execute_query(query)
    dict_result = {}

    if len(result) == 1:
        dict_result["id"] = result[0][0]
        dict_result["start"] = result[0][1]
        dict_result["stop"] = result[0][2]
        dict_result["mw"] = result[0][3]
        dict_result["complete"] = result[0][5]
        dict_result["seqADN"] = result[0][6]

    return dict_result


def get_all_applications_possibles():
    """
    Getting all the primary key of the table Applications_possibles
    :return a list of the result
    """
    query = "SELECT nom FROM Applications_possibles WHERE is_delete = 0;"
    result = execute_query(query)
    return result


def get_application_for_id(id=None):
    """
    Getting the applications of a product
    :param id : the GenBank id the of product
    :return a dict, with all the application of the product
    """
    if id is None:
        return ValueError

    else:
        query = "SELECT nom_app, validite, remarques FROM Applications WHERE is_delete = 0 AND id_produit =\"" + id + "\""
        results_temp = execute_query(query)
        results = []

        for temp in results_temp:
            dict = {}
            dict["nom_app"] = temp[0]
            dict["validite"] = temp[1]
            dict["remarque"] = temp[2]
            results.append(dict)

        return results


def get_organism_by_species(species):
    """
    Getting all the information of a species
    :param species: the name of the species
    :return: a dictionnary with all the information about the species {'attribute':value}
    """
    query = "SELECT * FROM Organisme WHERE espece = \"" + species + "\" AND is_delete = 0"
    results = execute_query(query)
    dict_result = {}
    if len(results) == 1:
        dict_result["species"] = results[0][0]
        dict_result["genus"] = results[0][1]
        dict_result["family"] = results[0][2]
        dict_result["order"] = results[0][3]
        dict_result["subclass"] = results[0][4]
        dict_result["classe"] = results[0][5]
        dict_result["phylum"] = results[0][6]
        dict_result["statut"] = results[0][7]
    return dict_result


def get_column_names(table):
    """
    Getting the names of all the columns of a table of the local DB
    :param table: the name of the table
    :return: a list of the columns names []
    """
    query = "PRAGMA table_info(" + table + ")"
    results = execute_query(query)
    names = []
    for result in results:
        names.append(result[1])
    return names


def get_all(table, attribute):
    """
    Getting all the values for an attribute of a table of the local DB
    :param table: the name of the table
    :param attribute: the name of the attribute
    :return: a list of all the values []
    """
    query = "SELECT DISTINCT " + attribute + " FROM " + table
    results = execute_query(query)
    datas = []
    for result in results:
        datas.append(result[0])
    return datas


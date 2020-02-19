import sqlite3 as s

database = "database\coraliotech_db.db" # the name of the local database


def commit_query(query):
    """commiting a query on the local database"""
    try:
        connection = s.connect(database)
        cursor = connection.cursor()
        cursor.execute("pragma foreign_keys = ON")
        cursor.execute(query)
        connection.commit()
        connection.close()
        return {'commited':True, 'error':''}
    except Exception as e:
        return {'commited':False, 'error':str(e)}


def execute_query(query):
    """executing a query on the local database"""
    connection = s.connect(database)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result


def get_query_insert(table, datas):
    """creating a query, type INSERT INTO"""
    begin = "INSERT INTO " + table + " ( "
    keys = (" , ").join(datas.keys())
    middle = " ) VALUES ( "
    values = (" , ").join(list(datas.values()))
    end = " );"
    query = begin + keys + middle + values + end
    return query


def get_product_by(id=None, name=None, species=None):
    """:return a dict, with all the value for a product, find by the id"""
    if id is not None:
        query = "SELECT * FROM Produit WHERE id =\"" + id + "\" AND is_delete = 0;"
    elif name is not None:
        query = "SELECT * FROM Produit WHERE nom =\"" + name + "\" AND is_delete = 0;"
    elif species is not None:
        query = "SELECT * FROM Produit WHERE espece =\"" + species + "\" AND is_delete = 0;"
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
    """:return a dict with all the value for a cds, find by id"""
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
    """:return all the value of the variable 'name' of the table Applications_possibles"""
    query = "SELECT nom FROM Applications_possibles WHERE is_delete = 0;"
    result = execute_query(query)
    return result


def get_application_for_id(id=None):
    """:return a dict, with all the application for a product"""
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

def get_column_names(table):
    query = "PRAGMA table_info(" + table + ")"
    results = execute_query(query)
    names = []
    for result in results:
        names.append(result[1])
    return names

def get_organism_by_species(species):
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



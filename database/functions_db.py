import sqlite3 as s

database = "database\coraliotech_test_db.db"


def commit_query(query):
    try:
        connection = s.connect(database)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
        return {'commited':True, 'error':''}
    except Exception as e:
        return {'commited':False, 'error':str(e)}


def execute_query(query):
    connection = s.connect(database)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result


def get_query_insert(table, datas):
    begin = "INSERT INTO " + table + " ( "
    keys = (" , ").join(datas.keys())
    middle = " ) VALUES ( "
    values = (" , ").join(list(datas.values()))
    end = " );"
    query = begin + keys + middle + values + end
    return query


def get_applications_possibles():
    query = "SELECT nom FROM Applications_possibles"
    result = execute_query(query)
    return result

def get_product_by(id=None, name=None, species=None):
    if id is not None:
        query = "SELECT * FROM Produit WHERE id =\"" + id + "\""
    elif name is not None:
        query = "SELECT * FROM Produit WHERE nom =\"" + name + "\""
    elif species is not None:
        query = "SELECT * FROM Produit WHERE espece =\"" + species + "\""
    else:
        return ValueError
    result = execute_query(query)
    dict_result = {}
    if len(result) == 1:
        dict_result["id"] = result[0][0]
        dict_result["name"] = result[0][1]
        dict_result["predicted"] = result[0][2]
        dict_result["delete"] = result[0][3]
        dict_result["source"] = result[0][4]
        dict_result["note"] = result[0][5]
        dict_result["species"] = result[0][6]
        dict_result["cds_id"] = result[0][7]
        dict_result["fonction"] = result[0][8]
    return dict_result


def get_cds_by(id_cds=None, id_product=None):
    if id_product is not None:
        id_cds = "cds_" + id_product
    query = "SELECT * FROM CDS WHERE id = \"" + id_cds + "\""
    result = execute_query(query)
    dict_result = {}
    if len(result) == 1:
        dict_result["id"] = result[0][0]
        dict_result["start"] = result[0][1]
        dict_result["stop"] = result[0][2]
        dict_result["mw"] = result[0][3]
        dict_result["delete"] = result[0][4]
        dict_result["complete"] = result[0][5]
        dict_result["seqADN"] = result[0][6]
    return dict_result






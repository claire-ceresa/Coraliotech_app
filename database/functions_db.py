import sqlite3 as s

database = "database\coraliotech_test_db.db"


def commit_query(query):
    try:
        connection = s.connect(database)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
        return True
    except:
        return False


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

def get_query_select():
    return


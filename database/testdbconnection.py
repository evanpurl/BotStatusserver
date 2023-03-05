from mysql.connector import Error, MySQLConnection
from database.python_mysql_dbconfig import read_db_config


def connect():  # Initial DB connection test
    """ Connect to MySQL database """

    db_config = read_db_config()
    conn = None
    try:
        conn = MySQLConnection(**db_config)
        if conn.is_connected():
            return True
        else:
            return False

    except Error as error:
        print("error")
        print(error)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
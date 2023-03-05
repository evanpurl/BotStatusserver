from mysql.connector import MySQLConnection, Error
from database.python_mysql_dbconfig import read_db_config


def findbots():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        if conn.is_connected():
            c = conn.cursor()

            sql = f"select * from bots"

            c.execute(sql)
            response = c.fetchall()
            if not response:
                return None
            c.close()  # Closes Cursor
            conn.close()  # Closes Connection
            return response
        else:
            return 'Connection to database failed.'
    except Error as e:
        print(e)
        return e
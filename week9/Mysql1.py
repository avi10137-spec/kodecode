import my_sql2
import time
import mysql.connector
def get_connection():
    return mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="secret",
    database="soldiers_db"
    )
def get_schema() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLE")
    # cursor.execute("DESCRIBE soldiers")
    rows = cursor.fetchall()
    print(rows)
    cursor.close()
    conn.close()
    return [{"column": row[0], "type": row[1]} for row in rows]

print(get_schema())

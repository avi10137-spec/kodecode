import mysql.connector
import time
time.sleep(2)
conn = mysql.connector.connect(
host="127.0.0.1", port=3306,
user="root", password="secret"
)
cur = conn.cursor()
cur.execute("SHOW DATABASES")
print("Databases:", [r[0] for r in cur.fetchall()])
cur.execute("USE solider_db")
cur.execute("SHOW TABLES")
print("Tables:", [r[0] for r in cur.fetchall()])
conn.close()
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="secret"
)
create_table_sql = """
CREATE TABLE IF NOT EXISTS soldiers (
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100) NOT NULL,
ranki VARCHAR(50),
unit VARCHAR(100),
active BOOLEAN DEFAULT TRUE
)
"""
cur.execute(create_table_sql)
conn.commit()
print("Table created successfully.")
print("Connected!")
# def get_connection():
#     return mysql.connector.connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="secret",
#     database="soldiers_db"
#     )
# def get_schema() -> list:
#     conn = get_connection()
#     cursor = conn.cursor()
#     create_table_sql = """
#     CREATE TABLE IF NOT EXISTS soldiers (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(100) NOT NULL,
#     ranki VARCHAR(50),
#     unit VARCHAR(100),
#     active BOOLEAN DEFAULT TRUE
#     )"""
#
#     cursor.execute(create_table_sql)
#     cursor.execute("SHOW TABLES")
#     # cursor.execute("DESCRIBE soldiers")
#     rows = cursor.fetchall()
#     print(rows)
#     # cursor.commit()
#     cursor.close()
#     conn.close()
#     return [{"column": row[0], "type": row[1]} for row in rows]
#
# print(get_schema())


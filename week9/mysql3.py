import mysql.connector
import time

time.sleep(2)
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="secret"
)
cur = conn.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS soldiers_db")
cur.execute("USE soldiers_db")
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
print("Table 'soldiers' created successfully inside 'soldiers_db'!")
cur.close()
conn.close()




def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="secret",
        database="soldiers_db"
    )


def get_schema() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DESCRIBE soldiers")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return [{"column": row[0], "type": row[1].decode('utf-8') if isinstance(row[1], bytes) else row[1]} for row in rows]
print("\n--- Soldiers Table Schema ---")
print(get_schema())
def create(name: str, ranki: str, unit: str,active:bool) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO soldiers (name, ranki, unit,active) VALUES (%s, %s, %s,%s)"
    values = (name, ranki, unit,active)
    cursor.execute(sql, values)
    conn.commit()
    new_id = cursor.lastrowid # MySQL give
    cursor.execute("SELECT * from soldiers")
    a=cursor.fetchall()
    print(a)
    cursor.close()
    conn.close()
    return new_id
# print(create("aharon","private","8200",False))
def update(soldier_id: int, data: dict) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    # Build the SET clause dynamically from the dict
    set_parts = [f"{key} = %s" for key in data.keys()]
    set_clause = ", ".join(set_parts)
    print(set_clause)
    sql = f"UPDATE soldiers SET {set_clause} WHERE id = %s"
    values = list(data.values()) + [soldier_id]
    print(values)
    cursor.execute(sql, values)
    conn.commit()
    changed = cursor.rowcount > 0 # False if id did not exist
    cursor.execute("SELECT * from soldiers")
    a = cursor.fetchall()
    print(a)
    cursor.close()
    conn.close()
    return changed
# update(2,{"name":"yosi","ranki":"privet"})
def delete(soldier_id: int) -> bool:

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM soldiers WHERE id = %s", (soldier_id,))
    conn.commit()
    deleted = cursor.rowcount > 0

    cursor.execute("SELECT * from soldiers")
    a = cursor.fetchall()
    print(a)
    cursor.close()
    conn.close()
    return deleted

# print(delete(3))
def get_all() -> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True) # returns dicts instead of tuples
    cursor.execute("SELECT * FROM soldiers")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
# print(get_all())
def get_by_id(soldier_id: int) -> dict | None:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers WHERE id = %s", (soldier_id,))
    row = cursor.fetchone() # returns one dict or None
    cursor.close()
    conn.close()
    return row
print(get_by_id(5))

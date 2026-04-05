import sqlite3

def query_sql(prompt):
    conn = sqlite3.connect("backend/data/sample.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sales LIMIT 5")
    return cursor.fetchall()

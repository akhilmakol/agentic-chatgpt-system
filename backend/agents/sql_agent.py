import sqlite3

def query_sql(prompt: str):
    conn = sqlite3.connect("backend/data/sample.db")
    cursor = conn.cursor()

    # Ensure table exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER,
        product TEXT,
        amount INTEGER
    )
    """)

    cursor.execute("INSERT INTO sales VALUES (1, 'Laptop', 1000)")
    cursor.execute("INSERT INTO sales VALUES (2, 'Phone', 500)")

    cursor.execute("SELECT * FROM sales")
    results = cursor.fetchall()

    conn.commit()
    conn.close()

    return results

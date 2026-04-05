import sqlite3

def get_connection():
    return sqlite3.connect("backend/data/sample.db")

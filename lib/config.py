import sqlite3
CONN = sqlite3.connect('parts.db')
CURSOR = CONN.cursor()

class Database:
    def create_tables(self):
        sql1 = """
        CREATE TABLE IF NOT EXISTS engine_part (
            engine_id INTEGER PRIMARY KEY  ,
            name TEXT NOT NULL,
            price INTEGER NOT NULL,
            part_no TEXT NOT NULL,
            part_description TEXT
        )
        """
        CURSOR.execute(sql1)
        sql2 = """
        CREATE TABLE IF NOT EXISTS body_part (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price INTEGER NOT NULL,
            part_no TEXT NOT NULL,
            part_description TEXT
        )
        """
        CURSOR.execute(sql2)
        sql3 = """
            CREATE TABLE IF NOT EXISTS light_part (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price INTEGER NOT NULL,
            part_no TEXT NOT NULL,
            part_description TEXT
"""       
        CURSOR.execute(sql3)
        CONN.commit()

def drop_tables(self):
    sql1 = "DROP TABLE engine_part"
    CURSOR.execute(sql1)
    sql2 = "DROP TABLE body_part"
    CURSOR.execute(sql2)
    sql3 = "DROP TABLE light_part"
    CURSOR.execute(sql3)
    CONN.commit()

db = Database()
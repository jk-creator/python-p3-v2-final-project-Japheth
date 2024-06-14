from lib.config import CONN, CURSOR

class Engine:
    @classmethod
    def create_engine(self):
        query = "INSERT INTO engine (name, price, part_no, part_description) VALUES (?, ?, ?, ?)"
        CURSOR.execute(query, (name, price, part_no, part_description))
        CONN.commit()
        return CURSOR.lastrowid
    
    @classmethod
    def get_engine_part_by_id(self, id):
        query = "SELECT * FROM engine_part WHERE id = ?"
        CURSOR.execute(query, (id,))
        return CURSOR.fetchone()
    
    @classmethod
    def update_engine_part_by_id(self, id, name, price, part_no, part_description):
        query = "UPDATE engine_part SET name = ?, price = ?, part_no = ?, part_description = ? WHERE id = ?"
        CURSOR.execute(query, (name, price, part_no, part_description, id))
        CONN.commit()
        return 

    @classmethod
    def delete_engine_part_by_id(self, id):
        query = "DELETE FROM engine_part WHERE id = ?"
        CURSOR.execute(query, (id,))
        CONN.commit()

    @classmethod
    def count_all_engine_parts(self):
        query = "SELECT COUNT(*) FROM engine_part"
        CURSOR.execute(query)
        return CURSOR.fetchone()

    @classmethod
    def get_all_engine_parts(self):
        query = "SELECT * FROM engine_part"
        CURSOR.execute(query)
        return CURSOR.fetchall()
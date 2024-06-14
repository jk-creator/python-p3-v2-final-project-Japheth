from lib.config import CONN, CURSOR

class Light:
    @classmethod
    def create_light_part(self, name, price, part_no, part_description):
        query = "INSERT INTO light_part (name, price, part_no, part_description) VALUES (?, ?, ?, ?)"
        CURSOR.execute(query, (name, price, part_no, part_description))
        CONN.commit()
        return CURSOR.lastrowid
    
    @classmethod
    def get_light_part_by_id(self, id):
        query = "SELECT * FROM light_part WHERE id = ?"
        CURSOR.execute(query, (id,))
        return CURSOR.fetchone()
    @classmethod
    def update_light_part_by_id(self, id, name, price, part_no, part_description):
        query = "UPDATE light_part SET name = ?, price = ?, part_no = ?, part_description = ? WHERE id = ?"
        CURSOR.execute(query, (name, price, part_no, part_description, id))
        CONN.commit()
    @classmethod
    def delete_light_part_by_id(self, id):
        query = "DELETE FROM light_part WHERE id = ?"
        CURSOR.execute(query, (id,))
        CONN.commit()
    @classmethod
    def count_all_light_parts(self):
        query = "SELECT COUNT(*) FROM light_part"
        CURSOR.execute(query)
        return CURSOR.fetchone()
    @classmethod
    def get_all_light_parts(self):
        query = "SELECT * FROM light_part"
        CURSOR.execute(query)
        return CURSOR.fetchall()
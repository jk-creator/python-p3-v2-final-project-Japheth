from lib.config import CONN, CURSOR

class Body:
    @classmethod
    def create_body_part(self, name, price, part_no, part_description):
        query = "INSERT INTO body_part (name, price, part_no, part_description) VALUES (?, ?, ?, ?)"
        CURSOR.execute(query, (name, price, part_no, part_description))
        CONN.commit()
        return CURSOR.lastrowid

    @classmethod
    def get_body_part_by_id(self, id):
        query = "SELECT * FROM body_part WHERE id = ?"
        CURSOR.execute(query, (id,))
        return CURSOR.fetchone()

    @classmethod
    def update_body_part_by_id(self, id, name, price, part_no, part_description):
        query = "UPDATE body_part SET name = ?, price = ?, part_no = ?, part_description = ? WHERE id = ?"
        CURSOR.execute(query, (name, price, part_no, part_description, id))
        CONN.commit()

    @classmethod
    def delete_body_part_by_id(self, id):
        query = "DELETE FROM body_part WHERE id = ?"

    def count_all_body_parts(self):
        query = "SELECT COUNT(*) FROM body_part"
        CURSOR.execute(query)
        return CURSOR.fetchone()

    def get_all_body_parts(self):
        query = "SELECT * FROM body_part"
        CURSOR.execute(query)
        return CURSOR.fetchall()
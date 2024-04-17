from db import connect_to_db

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

    def add_user(self):
        try:
            conn = connect_to_db()
            cursor = conn.cursor()

            query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
            values = (self.name, self.library_id)
            cursor.execute(query, values)

            conn.commit()
            print("User added successfully.")

        except Exception as e:
            print(f"Error adding user: {e}")

        finally:
            if conn:
                cursor.close()
                conn.close()
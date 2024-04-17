from db import connect_to_db

class Author:
    def __init__(self, name, biography):
        self._name = name
        self._biography = biography

        # connecting to database
        self.conn = connect_to_db()
        self.cursor = self.conn.cursor()
    def add_author(self):
        try:
            # Insert new author into Authors table
            query = "INSERT INTO Authors (author_name, biography) VALUES (%s, %s)"
            self.cursor.execute(query, (self._name, self._biography))
            self.conn.commit()
            print(f"{self._name} has been added to the library system!")

        except Exception as e:
            print(f"Error in Author __init__(): {e}")

        finally:
            # Close connection
            self.cursor.close()
            self.conn.close()

# Viewing authors in Authors table
    def view_authors():
        try:
            conn = connect_to_db()
            cursor = conn.cursor()

            query = "SELECT * FROM authors"
            cursor.execute(query)
            authors = cursor.fetchall()

            if authors:
                for author in authors:
                    print(author)
            else:
                print("No authors found.")

        except Exception as e:
            print(f"Error viewing authors: {e}")

        finally:
            if conn:
                cursor.close()
                conn.close()
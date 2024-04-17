from db import connect_to_db

#creating the class 
class Book:
    def __init__(self, title, author_id, genre_id, isbn, publication_date):
        self._title = title
        self._author_id = author_id
        self._genre_id = genre_id
        self._isbn = isbn
        self._publication_date = publication_date

        # connecting
        self.conn = connect_to_db()
        self.cursor = self.conn.cursor()
    def add_book(self):
        try:
            # Insert new book into Books table
            query = "INSERT INTO Books (title, author_id, genre_id, isbn, publication_date) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(query, (self._title, self._author_id, self._genre_id, self._isbn, self._publication_date))
            self.conn.commit()
            print(f"{self._title} has been added to the library system!")

        except Exception as e:
            print(f"Error in Book __init__(): {e}")

        finally:
            # close connection
            self.cursor.close()
            self.conn.close()

    def borrow_book(self,book_id):
        try:
            query = "UPDATE books SET availability = FALSE WHERE id = %s"
            self.cursor.execute(query, (book_id,))
            self.conn.commit()
            print("Book borrowed successfully.")
        except Exception as e:
            print(f"Error borrowing book: {e}")


    
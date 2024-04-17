from author import Author
from book import Book
from user import User
from db import connect_to_db



def main():
    try:
        # Establishing connection to the database
        conn = connect_to_db()
        if not conn:
            return
       

        while True:
            print("\n**** Main Menu ****")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                book_menu(Book)
            elif choice == "2":
                user_menu(User)
            elif choice == "3":
                author_menu(Author)
            elif choice == "4":
                print("Quitting the application.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Closing the database connection
        if conn:
            conn.close()

def book_menu(book_manager):
    try:
        while True:
            print("\n**** Book Operations ****")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                title = input("Enter book title: ")
                author_id = int(input("Enter author ID: "))
                genre_id = int(input("Enter genre ID: "))
                isbn = input("Enter book ISBN: ")
                publication_date = input("Enter publication date (YYYY-MM-DD): ")
                book_manager.add_book(title, author_id, genre_id, isbn, publication_date)
            elif choice == "2":
                user_id = int(input("Enter user ID: "))
                book_id = int(input("Enter book ID to borrow: "))
                book_manager.borrow_book(user_id, book_id)
            elif choice == "3":
                book_id = int(input("Enter book ID to return: "))
                book_manager.return_book(book_id)
            elif choice == "4":
                search_term = input("Enter search term (title or ISBN): ")
                books = book_manager.search_book(search_term)
                if books:
                    print("Search Results:")
                    for book in books:
                        print(book)
                else:
                    print("No matching books found.")
            elif choice == "5":
                books = book_manager.display_all_books()
                if books:
                    print("All Books:")
                    for book in books:
                        print(book)
                else:
                    print("No books found.")
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please enter a valid option.")
    except Exception as e:
        print(f"Error in book menu: {e}")

def user_menu(user_manager):
    try:
        while True:
            print("User Operations ****")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter user's name: ")
                library_id = input("Enter user's library ID: ")
                user_manager.add_user(name, library_id)
            elif choice == "2":
                user_id = int(input("Enter user ID: "))
                user_details = user_manager.view_user_details(user_id)
                if user_details:
                    print("User Details:")
                    print(user_details)
                else:
                    print("User not found.")
            elif choice == "3":
                users = user_manager.display_all_users()
                if users:
                    print("All Users:")
                    for user in users:
                        print(user)
                else:
                    print("No users found.")
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please enter a valid option.")
    except Exception as e:
        print(f"Error in user menu: {e}")

def author_menu(author_manager):
    try:
        while True:
            print("Author Operations")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter author's name: ")
                biography = input("Enter author's biography: ")
                author_manager.add_author(name, biography)
            elif choice == "2":
                author_id = int(input("Enter author ID: "))
                author_details = author_manager.view_author_details(author_id)
                if author_details:
                    print("Author Details:")
                    print(author_details)
                else:
                    print("Author not found.")
            elif choice == "3":
                authors = author_manager.display_all_authors()
                if authors:
                    print("All Authors:")
                    for author in authors:
                        print(author)
                else:
                    print("No authors found.")
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please enter a valid option.")
    except Exception as e:
        print(f"Error in author menu: {e}")
if __name__ == "__main__":
    main()

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="library_db"
)

cursor = db.cursor()

class Book:
    def __init__(self, book_id, title, author, available=True):
        self.id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author} | {'Available' if self.available else 'Unavailable'}"

class Member:
    def __init__(self, name):
        self.name = name
        cursor.execute("INSERT INTO members (name) VALUES (%s)", (name,))
        db.commit()
        cursor.execute("SELECT id FROM members WHERE name = %s", (name,))
        self.id = cursor.fetchone()[0]

    def borrow_book(self, book_id):
        cursor.execute("SELECT available FROM books WHERE id = %s", (book_id,))
        result = cursor.fetchone()

        if result and result[0]:
            cursor.execute("UPDATE books SET available = FALSE WHERE id = %s", (book_id,))
            cursor.execute("INSERT INTO borrowed_books (member_id, book_id) VALUES (%s, %s)", (self.id, book_id))
            db.commit()
            print(f"{self.name} borrowed book ID: {book_id}")
        else:
            print("Book is unavailable!")

    def return_book(self, book_id):
        cursor.execute("UPDATE books SET available = TRUE WHERE id = %s", (book_id,))
        cursor.execute("UPDATE borrowed_books SET return_date = CURRENT_TIMESTAMP WHERE member_id = %s AND book_id = %s",
                       (self.id, book_id))
        db.commit()
        print(f"{self.name} returned book ID: {book_id}")

class Library:
    def __init__(self):
        self.books = []
        self.load_books_from_db()

    def load_books_from_db(self):
        cursor.execute("SELECT id, title, author, available FROM books")
        self.books = [Book(*book) for book in cursor.fetchall()]

    def add_book(self, title, author):
        cursor.execute("INSERT INTO books (title, author, available) VALUES (%s, %s, TRUE)", (title, author))
        db.commit()
        self.load_books_from_db()

    def remove_book(self, book_id):
        cursor.execute("SELECT available FROM books WHERE id = %s", (book_id,))
        result = cursor.fetchone()

        if result and not result[0]:
            print("Book is currently borrowed and cannot be removed.")
        else:
            cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
            db.commit()
            self.load_books_from_db()

    def show_books(self):
        self.load_books_from_db()
        for book in self.books:
            print(book)

    def search_book(self, title):
        cursor.execute("SELECT id, title, author, available FROM books WHERE title LIKE %s", (f"%{title}%",))
        results = cursor.fetchall()

        if results:
            for book in results:
                print(f"{book[1]} by {book[2]} | {'Available' if book[3] else 'Unavailable'}")
        else:
            print(f"{title} not found!")

def main():
    library = Library()

    library.add_book("1984", "George Orwell")
    library.add_book("Brave New World", "Aldous Huxley")

    print("\nAvailable Books:")
    library.show_books()

    member1 = Member("Donnie")
    member2 = Member("Alice")

    print("\nBorrowing Books:")
    member1.borrow_book(1)
    member2.borrow_book(2)

    print("\nLibrary After Borrowing:")
    library.show_books()

    print("\nReturning Books:")
    member1.return_book(1)

    print("\nFinal Library Status:")
    library.show_books()

    print("\nSearching for a Book:")
    library.search_book("1984")

if __name__ == "__main__":
    main()
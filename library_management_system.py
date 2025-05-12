class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._available = True

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, status):
        self._available = status

    def __str__(self):
        return f"{self._title} by {self._author} | {'available' if self._available else 'unavailable'}"

class Member:
    def __init__(self, name):
        self._name = name
        self._borrowed_books = []

    def borrow_book(self, book):
        if len(self._borrowed_books) < 3 and book.available:
            book.available = False
            self._borrowed_books.append(book)
        else:
            print('You\'ve reached the borrowing limit!')
    
    def return_book(self, book):
        if book in self._borrowed_books:
            book.available = True
            self._borrowed_books.remove(book)
        else:
            print('You\'ve never borrowed that book!')

    def __str__(self):
        return f'Member: {self._name} | Borrowed Books: {len(self._borrowed_books)}'

class PremiumMember(Member):
    def borrow_book(self, book):
        if book.available:
            book.available = False
            self._borrowed_books.append(book)
        else:
            print(f'{book._title} is unavailable!')

class Library():
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            if book.available:
                print(f"{book._title} is current being borrowed and can't be remove")
            else:
                self.books.remove(book)
        else:
            print(f'{book._title} is not in the library!')

    def show_books(self):
        for book in self.books:
            print(book)
    
    def search_book(self, title):
        matches = [book for book in self.books if title.lower() in book._title.lower()]

        for book in self.books:
            if title == book._title:
                print(book)
                return book
        print(f'{title} is not found!')

    @staticmethod
    def is_available(book):
        return book.available
    
    @classmethod
    def generate_library(cls, book_list):
        library = cls()
        for title, author in book_list:
            library.add_book(Book(title, author))
        return library

    def __len__(self):
        return len(self.books)

def main():
    book_list = [
        ("1984", "George Orwell"),
        ("Brave New World", "Aldous Huxley"),
        ("To Kill a Mockingbird", "Harper Lee"),
        ("The Catcher in the Rye", "J.D. Salinger"),
        ("The Great Gatsby", "F. Scott Fitzgerald")
    ]
    
    library = Library.generate_library(book_list)

    member1 = Member("Donnie")
    premium_member1 = PremiumMember("Alice")

    print("\nAvailable Books:")
    library.show_books()

    print("\nBorrowing Books:")
    member1.borrow_book(library.books[0])  # Donnie borrows "1984"
    premium_member1.borrow_book(library.books[2])  # Alice borrows "To Kill a Mockingbird"

    print("\nLibrary After Borrowing:")
    library.show_books()

    print("\nReturning a Book:")
    member1.return_book(library.books[0])  # Donnie returns "1984"

    print("\nFinal Library Status:")
    library.show_books()

    print("\nSearching for a Book:")
    library.search_book("The Great Gatsby")

if __name__ == "__main__":
    main()
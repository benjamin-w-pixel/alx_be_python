# library_management.py

class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """
        Initialize a book with title and author.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute
    
    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages books."""
    
    def __init__(self):
        """Initialize the library with an empty book collection."""
        self._books = []  # Private list to store books
    
    def add_book(self, book):
        """
        Add a book to the library's collection.
        
        Args:
            book (Book): The book to add
        """
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book objects can be added to the library")
    
    def find_book(self, title):
        """
        Find a book by its title (case-insensitive).
        
        Args:
            title (str): The title to search for
            
        Returns:
            Book: The book if found, None otherwise
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def check_out_book(self, title):
        """
        Check out a book from the library.
        
        Args:
            title (str): The title of the book to check out
            
        Returns:
            bool: True if successful, False otherwise
        """
        book = self.find_book(title)
        if book and book.check_out():
            return True
        return False
    
    def return_book(self, title):
        """
        Return a book to the library.
        
        Args:
            title (str): The title of the book to return
            
        Returns:
            bool: True if successful, False otherwise
        """
        book = self.find_book(title)
        if book and book.return_book():
            return True
        return False
    
    def list_available_books(self):
        """Print all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books currently available")
        else:
            for book in available_books:
                print(book)
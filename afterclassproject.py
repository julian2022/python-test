# ── BOOK CLASS ─────────────────────────────────────────────────
# : Define a class called Book
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    # : Define borrow(self)
    #   If self.is_borrowed is already True → print that it's already borrowed
    #   Otherwise → set self.is_borrowed = True and print a borrow message
    def borrow(self):
        if self.is_borrowed:
            print(f"{self.title} is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"{self.title} has been borrowed.")

    # : Define return_book(self)
    #   If self.is_borrowed is False → print that it wasn't borrowed
    #   Otherwise → set self.is_borrowed = False and print a return message
    def return_book(self):
        if not self.is_borrowed:
            print(f"{self.title} was not borrowed.")
        else:
            self.is_borrowed = False
            print(f"{self.title} has been returned.")

    # : Define __str__(self)
    #   Return a string like:  "Title by Author [Available]"
    #   or                     "Title by Author [Borrowed]"
    def __str__(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"{self.title} by {self.author} [{status}]"


# ── LIBRARY ────────────────────────────────────────────────────
# : Create at least 3 Book objects with different titles and authors
book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("Clean Code", "Robert C. Martin")
book3 = Book("The Pragmatic Programmer", "Andy Hunt")

print("=" * 42)
print("         📚  LIBRARY SYSTEM")
print("=" * 42)

# : Print each book (uses __str__ automatically)
print(book1)
print(book2)
print(book3)

# : Borrow some books using .borrow()
book1.borrow()
book2.borrow()

# : Try to borrow the same book twice to test the guard message
book1.borrow()

# : Return a book using .return_book()
book1.return_book()

# : Try to return a book that was never borrowed to test that guard
book3.return_book()

# : Print each book again to show updated status
print("\nUpdated library status:")
print(book1)
print(book2)
print(book3)
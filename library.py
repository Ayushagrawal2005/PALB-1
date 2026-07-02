class Library:
    def __init__(self, name):
        self.books = []
        self.name = name

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def get_book(self):
        return self.books

    def no_of_books(self):
        return print(f"Number of books in {self.name}: {len(self.books)}")


b1 = Library("Python Programming")
b2 = Library("Data Structures")
b3 = Library("Algorithms")
b4 = Library("Machine Learning")

b1.add_book("Python Programming")
b2.add_book("Data Structures")
b3.add_book("Algorithms")
b4.add_book("Machine Learning")
b3.add_book("Advanced Python")
b4.add_book("Deep Learning")
b1.remove_book("Python Programming")
print(b2.no_of_books())
print(b1.no_of_books())
print(b3.no_of_books())
print(b4.no_of_books())
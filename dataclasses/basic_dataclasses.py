from dataclasses import dataclass

# with no default values
@dataclass
class Book:
    title: str
    author: str
    year: int

book = Book("<book_title>", "<book_author>", 1949)
print(book)

# with default values
@dataclass
class Book:
    title: str
    author: str
    year: int = 2023  # Default value

book1 = Book("<book_title>", "<book_author>", 1949)
book2 = Book("<book_title>", "<book_author>")  # Uses default year
print(book1, book2)

# dataclass with an added behavior
@dataclass
class Book:
    title: str
    author: str
    year: int

    def age(self) -> int:
        current_year = 2023
        return current_year - self.year

book = Book("<book_title>", "<book_author>", 1949)
print(f"The book is {book.age()} years old.")
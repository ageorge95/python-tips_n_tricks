from dataclasses import dataclass

@dataclass(frozen=True)
class Book:
    title: str
    author: str
    year: int

book = Book("<book_title>", "<book_author>", 1949)
book.title = "New Title"  # Raises an error because the dataclass is frozen

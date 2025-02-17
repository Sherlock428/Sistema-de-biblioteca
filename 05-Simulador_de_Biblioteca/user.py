from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    rating: int
    library_books: list
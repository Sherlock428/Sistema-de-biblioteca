from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    library_books: list
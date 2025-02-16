from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Books:
    id: int
    title: str
    author: str
    avaliable: bool


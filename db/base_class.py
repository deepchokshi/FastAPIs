import re
from typing import Any

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative

@as_declarative
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        name = re.sub(r"(?<!^)(?=[A-Z])","_", cls.__name__)  #Read_Book
        return name.lower()
        # Books, ReadBook -> books, read_book
from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    category: str

    class Config:
        schema_extra = {
            'example': {
                "title": "Book Title",
                "author": "Name of Author",
                "category": "Category"
            }
        }

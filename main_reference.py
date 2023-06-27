from fastapi import FastAPI, HTTPException, Depends
from schema import Book
from starlette import status
from setting import PostgresConfiguration
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import model

app = FastAPI()

books = [
    {"title": "Title One", "author": "Author One", "category": "Data Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Data Analysis"},
    {"title": "Title Three", "author": "Author One", "category": "Python Developer"},
    {"title": "Title Four", "author": "Author Two", "category": "Data Science"}
]

pg = PostgresConfiguration()
engine = create_engine(pg.postgres_db_path)

model.Base.metadata.create_all(engine, checkfirst=True)

SessionLocal = sessionmaker(autoflush=True, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/books/allbooks", tags=["Book"])
async def get_all_books(db: Session = Depends(get_db)):
        book_data = db.query(model.Book).all()
        books = []
        if not book_data:
            raise HTTPException(status_code=404, detail="Book Not Found")
        for book in book_data:
            books.append({"Title": book.title, "Author": book.author, "Category": book.category})
        return books


@app.get("/books/{title}", tags=["Book"])
async def get_books_by_title(title: str):
    res = []
    for book in books:
        # db.query(model.Book).filter(model.Book.title == title).first()
            res.append(book)
    if res:
        return res
    raise HTTPException(status_code=404, detail=f"Book not found with {title}")


@app.post("/books/add_book", status_code=status.HTTP_201_CREATED, tags=["Book"])
async def add_books(req: Book, db: Session = Depends(get_db)):
    if req:
        req = req.dict(exclude_unset=True)
        data = {"title": req["title"], "author": req["author"], "category": req["category"]}
        book_data = model.Book(**data)
        db.add(book_data)
        db.commit()
        return book_data.id
    else:
        raise HTTPException(status_code=401, detail="Enter correct books details")


@app.patch("/books/{title}/update_category", tags=["Book"])
async def update_category_book_by_title(title: str, req: dict):
    for book in books:
        if book["title"] == title:
            book["category"] = req["category"]
            break
    else:
        raise HTTPException(status_code=404, detail=f"Book with Title:{title} Not Found")


@app.put("/books/{title}/update", tags=["Book"])
async def update_book_by_title(title: str, req: dict):
    for book in books:
        if book["title"] == title:
            book["title"] = req["title"]
            book["author"] = req["author"]
            book["category"] = req["category"]
            break
    else:
        raise HTTPException(status_code=404, detail=f"Book with Title:{title} Not Found")


@app.get("/books/", tags=["Book"])
async def get_books_by_category(xyz: str):
    res = []
    for book in books:
        if book["category"] == xyz:
            res.append(book)
    if res:
        return res
    raise HTTPException(status_code=404, detail=f"Book not found with category: {xyz}")


@app.post("/e-books/create", tags=["E-Book"])
async def add_e_book(req: dict):
    print(req)
    print(req)

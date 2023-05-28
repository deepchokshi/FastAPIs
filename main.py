from fastapi import FastAPI, HTTPException
from schema import Book
from starlette import status
app = FastAPI()


@app.get("/books/allbooks", tags=["Book"])
async def get_all_books():
    if books:
        return books
    return "No book Found"


@app.get("/books/{title}", tags=["Book"])
async def get_books_by_title(title: str):
    res = []
    for book in books:
        if book["title"] == title:
            res.append(book)
    if res:
        return res
    raise HTTPException(status_code=404, detail=f"Book not found with {title}")


@app.post("/books/add_book", status_code=status.HTTP_201_CREATED, tags=["Book"])
async def add_books(req: Book):
    if req:
        books.append(req)

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
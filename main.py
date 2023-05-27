from fastapi import FastAPI, HTTPException

app = FastAPI()

books = [
    {"title": "Title One", "author": "Author One", "category": "Data Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Data Analysis"},
    {"title": "Title Three", "author": "Author One", "category": "Python Developer"},
    {"title": "Title Four", "author": "Author Two", "category": "Data Science"}
]


@app.get("/books/allbooks")
async def get_all_books():
    if books:
        return books
    return "No book Found"


@app.get("/books/{title}")
async def get_books_by_title(title: str):
    res = []
    for book in books:
        if book["title"] == title:
            res.append(book)
    if res:
        return res
    raise HTTPException(status_code=404, detail=f"Book not found with {title}")


@app.post("/books/add_book")
async def add_books(req: dict):
    if req:
        books.append(req)
        return books
    else:
        raise HTTPException(status_code=401, detail="Enter correct books details")


@app.patch("/books/{title}/update_category")
async def update_category_book_by_title(title: str, req: dict):
    for book in books:
        if book["title"] == title:
            book["category"] = req["category"]
            break
    else:
        raise HTTPException(status_code=404, detail=f"Book with Title:{title} Not Found")


@app.put("/books/{title}/update")
async def update_book_by_title(title: str, req: dict):
    for book in books:
        if book["title"] == title:
            book["title"] = req["title"]
            book["author"] = req["author"]
            book["category"] = req["category"]
            break
    else:
        raise HTTPException(status_code=404, detail=f"Book with Title:{title} Not Found")


@app.get("/books/")
async def get_books_by_category(xyz: str):
    res = []
    for book in books:
        if book["category"] == xyz:
            res.append(book)
    if res:
        return res
    raise HTTPException(status_code=404, detail=f"Book not found with category: {xyz}")
import os

from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import ORJSONResponse, FileResponse

PORT = 8000

app = FastAPI(default_response_class=ORJSONResponse)

# pdfは静的ファイルとして
app.mount("/books", StaticFiles(directory="books", html=True), name="static")


# index.html
@app.get("/")
async def index():
    return FileResponse("index.html")


# search.js
@app.get("/search.js")
async def searchJS():
    return FileResponse("search.js")


# 本の一覧
@app.get("/list-books")
async def booksList():
    books_dir = "books"
    if not os.path.exists(books_dir):
        raise HTTPException(404, "Books directory not found")
    files = [f for f in os.listdir(books_dir) if f.endswith(".pdf")]
    return files


# pdfjs mjsがロードされないので面倒な方法で実装しています
@app.get("/pdfjs/{path:path}")
async def pdfjs(request: Request, path: str):
    # 必要になったら
    # params = request.query_params.get("file")
    path = path.replace("../", "")
    if path.endswith(".mjs"):
        contentType = "application/javascript"
        print("a")
    else:
        contentType = None
    return FileResponse(f"pdfjs/{path}", media_type=contentType)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=PORT)

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from utils import download


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    return HTMLResponse(open("static/index.html", "r").read())


class Item(BaseModel):
    message: str


@app.post("/youtube")
async def youtube(item: Item):
    download(item.message)
    return {"message": f"Hello {item.message}"}

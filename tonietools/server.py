from typing import List, Optional

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from tonietools.youtube_importer import import_youtube_video


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    import os

    cwd = os.getcwd()
    print(cwd)
    return HTMLResponse(open("static/index.html", "r").read())


class Video(BaseModel):
    url: str
    name: Optional[str]
    start: Optional[str]
    end: Optional[str]


@app.post("/youtube")
async def youtube(videos: List[Video]):
    for v in videos:
        import_youtube_video(v.url, v.name, v.start, v.end)
    return f"Uploaded {len(videos)} items"


def run_server(host="0.0.0.0", port=8000):
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    run_server()

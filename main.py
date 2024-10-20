from typing import Optional

from fastapi import FastAPI
import instaloader

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ins/{item_id}")
def ins_item(item_id: str, q: Optional[str] = None):
    L = instaloader.Instaloader()
    if item_id=='':
        item_id='likelook.by'
    username = item_id
    profile = instaloader.Profile.from_username(L.context, username)
    sss=''
    for post in profile.get_posts():
       sss= sss+post.caption
    return {"message": sss}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    L = instaloader.Instaloader()
    username = 'likelook.by'
    profile = instaloader.Profile.from_username(L.context, username)
    for post in profile.get_posts():
        q=q+post.caption
    return {"item_id": item_id, "q": q}

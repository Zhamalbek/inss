from typing import Optional
from fastapi import FastAPI
import instaloader

L = instaloader.Instaloader()
username = 'likelook.by'
profile = instaloader.Profile.from_username(L.context, username)
sss='';
for post in profile.get_posts():
    print(post.caption)
    sss=sss+post.caption
    
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ins/{item_id}")
def ins_item(item_id: str, q: Optional[str] = None):
    global sss
    return {"message": sss}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    global sss
    return {"item_id": item_id, "q": q,"sss":sss}

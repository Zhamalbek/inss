from typing import Optional
from fastapi import FastAPI
from openai import OpenAI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ins/{item_id}")
def ins_item(item_id: str, q: Optional[str] = None):
    return {"message": item_id}

@app.get("/items/{item_id}")
def read_item(item_id: int, q):
    base_url = "https://api.aimlapi.com/v1"
    system_prompt = "You are a travel agent. Be descriptive and helpful."
    user_prompt = "Tell me about San Francisco"
    api2 = OpenAI(api_key=api_key, base_url=base_url)
    completion = api2.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=256,
    )

    response = completion.choices[0].message.content

    print("User:", user_prompt)
    print("AI:", response)
    q=user_prompt+'--'+response
    return {"item_id": item_id, "q": q}

@app.get("/{item_id}/{q}")
def vvv_item(item_id: str, q: str):
    return {"item_id": item_id, "q": q}

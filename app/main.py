import os
from typing import Union
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.LLM import LLM

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


llm = LLM()


@app.get("/users/me")
def read_current_user(Authorization: Union[str, None] = Header(default=None)):
    if Authorization == os.getenv("API_KEY"):
        return {"response": "ok"}
    else:
        return {"response": "false"}


class Post(BaseModel):
    content: str


@app.post("/api/llm/{post_id}")
def summerize_post(
    post_id: int, post: Post, Authorization: Union[str, None] = Header(default=None)
):
    if Authorization == os.getenv("API_KEY"):
        raw_content = post.content
        clean_text = llm.summarize_text(raw_content)
        return {"id": post_id, "content": clean_text, "raw_content": raw_content}
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")

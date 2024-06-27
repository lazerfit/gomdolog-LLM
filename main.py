from typing import Annotated
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from bs4 import BeautifulSoup as bs
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

origins = ["http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

security = HTTPBasic()


@app.get("/api/llm/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/me")
def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {"username": credentials.username, "password": credentials.password}


class Post(BaseModel):
    content: str


def remove_html_tags(text):
    soup = bs(text, "lxml")
    clean_text = soup.text
    return clean_text


@app.post("/api/llm/{post_id}")
def summerize_post(post_id: int, post: Post):
    raw_content = post.content
    clean_text = remove_html_tags(raw_content)
    return {"id": post_id, "content": clean_text, "raw_content": raw_content}

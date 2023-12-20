from app.database import DataBase
from app.model import Model
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pandas as pd

df = pd.read_csv('titles.csv')


class Item(BaseModel):
    text: str


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

model = Model()

settings = {
    "name": "arxiv"
}
db = DataBase(settings)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/embedding/")
async def get_embedding(item: Item):
    embedding = model.embedding(item.text)
    return {'embedding': embedding.tolist()}


@app.post("/add/")
async def get_embedding(item: Item):
    embedding = model.embedding(item.text)
    db.add([item.text], embedding)
    return {'embedding': embedding.tolist()}


@app.post("/query/")
async def get_embedding(item: Item):
    embedding = model.embedding(item.text)
    results = db.query_embedding(embedding)
    urls = results["metadatas"][0]
    titles = []
    for item in urls:
        full_row = df.loc[df['_url'] == item['url']]
        title = full_row['_title'].values[0]
        titles.append(title)
    results['titles'] = titles
    return results

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/news")
def get_news():
    return [{"id": 1, "title": "First News Item", "content": "This is a placeholder news item."}]

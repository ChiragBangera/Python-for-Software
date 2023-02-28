from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel


app = FastAPI()


@app.get("/test", response_class=JSONResponse)
def test_endpoint():
    return {"test key": "some value", "another key": "some other value"}


@app.get("/")
def home():
    return "Welcome"

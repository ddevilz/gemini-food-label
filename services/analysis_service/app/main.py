from fastapi import FastAPI, Request
from .routers import gemini
from fastapi.responses import HTMLResponse


app = FastAPI()

app.include_router(gemini.router)

@app.get('/', response_class=HTMLResponse)
def root(request: Request):
    return "<h1> Hello World!</h1>"
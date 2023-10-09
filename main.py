from fastapi import FastAPI

app = FastAPI()

@app.router.get('/')
def first():
    return "Hello World!"
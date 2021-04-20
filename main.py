from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Henrique'}}

@app.get('/about')
def about():
    return "Hefesto with FastAPI in Python"